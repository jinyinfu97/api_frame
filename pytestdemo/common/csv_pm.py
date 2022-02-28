import csv
import json

import jsonpath
import yaml

from pytestdemo.common.read_config_file import basicurl, read_data_yaml, read_csv_data


def read_testcase_csv(yaml_path):
    with open(basicurl() + yaml_path, encoding='utf-8') as f:
        caseinfo = yaml.load(f, Loader=yaml.FullLoader)

        if len(caseinfo) >= 2:
            return caseinfo
        else:
            if "parameterize" in dict(*caseinfo).keys():
                new_caseinfo = ddt(*caseinfo)
                # print(new_caseinfo)
                return new_caseinfo
            else:
                return caseinfo


def ddt(caseinfo):
    if "parameterize" in caseinfo.keys():
        caseinfo_str = json.dumps(caseinfo)
        for param_key, param_value in caseinfo["parameterize"].items():
            key_list = param_key.split("-")
            # 规范yaml数据文件的写法
            length_flag = True

            data_list = read_csv_data(param_value)

            for data in data_list:
                if len(data) != len(key_list):
                    length_flag = False
                    break
            # 替换值
            new_caseinfo = []
            if length_flag:
                for x in range(1, len(data_list)):  # 循环数据行数
                    temp_caseinfo = caseinfo_str
                    for y in range(0, len(data_list[x])):  # 循环数据列
                        if data_list[0][y] in key_list:
                            # 替换原始的yaml里面的$ddt{}
                            if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                                temp_caseinfo = temp_caseinfo.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                      str(data_list[x][y]))
                            elif isinstance(data_list[x][y], dict) or isinstance(data_list[x][y], list):
                                temp_caseinfo = temp_caseinfo.replace('"$ddt{' + data_list[0][y] + '}"',
                                                                      json.dumps(data_list[x][y]))
                            else:
                                temp_caseinfo = temp_caseinfo.replace("$ddt{" + data_list[0][y] + "}",
                                                                      str(data_list[x][y]))

                    new_caseinfo.append(json.loads(temp_caseinfo))
            return new_caseinfo
    else:
        return caseinfo





if __name__ == '__main__':
    # print(read_testcase_csv('/testcases/fund_login/login_data.yaml'))
    yq = 'equal(Success=true)'

    # | name = jinxin
    # for key, value in yq.items():
    #     if key == 'status_code':
    #         if value != self.status_code:
    #             print(f'状态码不等于{value}')
    #             flag = flag + 1
    #     else:
    #         print(f'json提取之前的响应值为{self.return_json}')
    #         lists = jsonpath.jsonpath(self.return_json, f"$..{key}")
    #         print(f'json提取的值为{lists}')
    #         if lists:
    #             if value != jsonpath.jsonpath(self.return_json, f"$..{key}")[0]:
    #                 print(f'{key}的值不等于{value}')
    #                 flag = flag + 1
    #         else:
    #             flag = flag + 1
    #             print("断言失败：返回的结果中不存在：" + key)
    # return flag
