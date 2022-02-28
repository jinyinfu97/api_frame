import json
import re
import jsonpath
import requests
from pytestdemo.common.read_config_file import write_extract, read_config_yaml
from pytestdemo.log.python_logging import logFrame


class RequestsUtil:
    def __init__(self, obj, baseurl):
        self.obj = obj
        self.status_code = ''
        self.return_text = ''
        self.return_json = ''
        self.baseurl = baseurl

    def send_requests(self, method, url, headers, **kwargs):
        if headers != None:
            headers = self.repalce(headers)
        for key, value in kwargs.items():
            if key in ['json', 'data', 'params']:
                kwargs[key] = self.repalce(value)
            else:
                print('json', 'data', 'params', 'headers不在里面')
        aaa = read_config_yaml('base', self.baseurl) + self.repalce(url)
        logFrame().logger_info(f'完整的请求url为  {aaa}')
        logFrame().logger_info(f'剩余请求参数为  {kwargs}')
        res = requests.session().request(method=method, headers=headers,
                                         url=read_config_yaml('base', self.baseurl) + self.repalce(url), **kwargs)
        return res

    def anylasic_testcase(self, caseinfo):

        if caseinfo['name'] and caseinfo['request']['url'] and caseinfo['request']['method']:
            logFrame().logger_info(f'{caseinfo["name"]}接口测试开始！！')
            logFrame().logger_info(f'请求方式为{caseinfo["request"]["method"]}')
            url = caseinfo['request'].pop('url')
            method = caseinfo['request'].pop('method')
            headers = None
            if 'headers' in caseinfo['request'].keys():
                headers = caseinfo['request'].pop('headers')
            res = self.send_requests(method=method, url=url, headers=headers, **caseinfo['request'])
            caseinfo['request']['url'] = url
            caseinfo['request']['method'] = method
            caseinfo['request']['headers'] = headers
            logFrame().logger_info(f'{caseinfo["name"]}接口的响应结果为{res.text}')
            logFrame().logger_info(f'{caseinfo["name"]}接口测试结束！！+\n')
            self.status_code = res.status_code
            self.return_text = res.text
            try:
                self.return_json = res.json()
            except Exception as erro:
                print(f'相应结果不支持json格式，错误信息为{erro}')
            for key, value in caseinfo.items():
                if key == 'extract':

                    extract_data = self.repalce(caseinfo['extract'])
                    for extract_key, extract_value in extract_data.items():
                        if str(extract_key).split('&')[0] in self.return_text:
                            if "(.+?)" in extract_value or '(.*?)' in extract_value:
                                return_text = re.search(extract_value, self.return_text).group(1)
                                return_value = {extract_key: return_text}
                                write_extract(return_value)
                            else:
                                self.return_json = res.json()
                                return_json = jsonpath.jsonpath(self.return_json, extract_value)[0]
                                return_value = {extract_key: return_json}
                                write_extract(return_value)
            # 断言封装
            if caseinfo['validate']:
                self.assert_value(caseinfo['validate'])
            return res
        else:
            print('一级关键字name和url,method不存在！！！')

    def assert_value(self, lx):
        all_flag = 0
        for n in lx:
            for key, value in n.items():
                if key == 'eq' and 'equal(' not in value:
                    flag = self.assert_equal(value)
                    all_flag = all_flag + flag
                elif key == 'eq' and 'equal(' in value:
                    flag = self.assert_equal_csv(value)
                    all_flag = all_flag + flag
                elif key == 'contain' and 'contain(' in value:
                    flag = self.assert_contain_csv(value)
                    all_flag = all_flag + flag
                elif key == 'contain' and 'contain(' not in value:
                    flag = self.assert_contain(value)
                    all_flag = all_flag + flag
                else:
                    print('该框架不支持该断言方式！！')
        # print(all_flag)
        assert all_flag == 0

    # 当断言封装在yaml中时
    def assert_equal(self, yq):
        flag = 0
        for key, value in yq.items():
            if key == 'status_code':
                if value != self.status_code:
                    print(f'状态码不等于{value}')
                    flag = flag + 1
            else:
                lists = jsonpath.jsonpath(self.return_json, f"$..{key}")
                if lists:
                    if value != jsonpath.jsonpath(self.return_json, f"$..{key}")[0]:
                        print(f'{key}的值不等于{value}')
                        flag = flag + 1
                else:
                    flag = flag + 1
                    print("断言失败：返回的结果中不存在：" + key)
        return flag

    # 当断言封装在csv中时
    def assert_equal_csv(self, yq):
        flag = 0
        start_index = yq.index('(') + 1
        end_index = yq.index(')')
        if 'equal' in str(yq) and '|' in str(yq):
            yq_list = yq[start_index:end_index].split('|')
            for n in yq_list:
                key = n.split('=')[0]
                lists = jsonpath.jsonpath(self.return_json, f"$..{key}")
                if lists:
                    value = n.split('=')[1]
                    if value != str(jsonpath.jsonpath(self.return_json, f"$..{key}")[0]):
                        print(f'{key}的值不等于{value}')
                        flag = flag + 1
                else:
                    flag = flag + 1
                    print("断言失败：返回的结果中不存在：" + key)
        else:
            key = yq[start_index:end_index].split('=')[0]
            lists = jsonpath.jsonpath(self.return_json, f"$..{key}")
            if lists:
                value = yq[start_index:end_index].split('=')[1]
                if value != str(jsonpath.jsonpath(self.return_json, f"$..{key}")[0]):
                    print(f'{key}的值不等于{value}')
                    flag = flag + 1
            else:
                flag = flag + 1
                print("断言失败：返回的结果中不存在：" + key)
        return flag

    # 当断言封装在yaml中时
    def assert_contain(self, yq):
        flag = 0
        for n in yq:
            if str(n) not in self.return_text:
                flag = flag + 1
                print(f'{n}不在响应信息里！！')
        return flag

    # 当断言封装在csv中时
    def assert_contain_csv(self, yq):
        flag = 0
        start_index = yq.index('(')
        end_index = yq.index(')')
        if 'contain' in str(yq) and '|' in str(yq):
            yq_list = yq[start_index + 1:end_index].split('|')
            for n in yq_list:
                if str(n) not in self.return_text:
                    flag = flag + 1
                    print(f'{n}不在响应信息里！！')
        else:
            if yq[start_index + 1:end_index] not in self.return_text:
                flag = flag + 1
                print(f'{yq[start_index + 1:end_index]}不在响应信息里！！')
        return flag

    def repalce(self, data):
        # 转化为字符串
        datatype = type(data)
        if isinstance(data, list) or isinstance(data, dict):
            string = json.dumps(data)
        else:
            string = str(data)
        for a in range(string.count('${')):
            if '${' in string and '}' in string:
                start_index = string.index('${')
                end_index = string.index('(')
                old_value = string[start_index:end_index + 1]
                fun_name = old_value[2:-1]
                func = getattr(self.obj, fun_name)
                args = string[string.index('(') + 1:string.index(')')].split(',')
                if '' in args:
                    new_value = func()
                else:
                    new_value = func(*args)
                s = string.index('${')
                e = string.index('}')
                v = string[s:e + 1]
                if isinstance(new_value, int) or isinstance(new_value, float):
                    string = string.replace('"' + str(v) + '"', str(new_value))
                else:
                    string = string.replace(str(v), str(new_value))
                # print(f'替换后的数据为{string}')

        if isinstance(data, list) or isinstance(data, dict):
            data = json.loads(string)
        else:
            data = datatype(string)
        return data


if __name__ == '__main__':
    tx = "张启娣天天基金登录成功用例,15618392885,${md5(zqd1234qwer)},contain(UToken|CToken),equal(Success=true)"
