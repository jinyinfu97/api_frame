import json

import yaml

from pytestdemo.common.read_config_file import basicurl, read_data_yaml


# def read_case(path):
#     with open(basicurl()+path, mode='r+', encoding='utf-8') as f:
#         caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
#         if len(caseinfo)>=2:
#             return caseinfo
#         else:
#             if 'parametrize' in dict(caseinfo[0]).keys():
#                 newcaseinfo = ddt(caseinfo[0])
#                 print(newcaseinfo)
#                 return newcaseinfo
#             else:
#                 return caseinfo
# def ddt(newcaseinfo):
#     case_list= []
#     data = read_case(list(dict(newcaseinfo['parametrize']).values())[0])
#     # num是数据驱动列表
#     for num in data:
#         if len(list(newcaseinfo["parametrize"].keys())[0].split('-')) != len(num):
#             print('数据驱动参数个数存在问题！！！')
#             return newcaseinfo
#     for x in range(1, len(data)):
#         tmp = json.dumps(newcaseinfo)
#         for y in range(0, len(data[x])):
#
#             if isinstance(data[x][y], int) or isinstance(data[x][y], float):
#                 tmp = tmp.replace('"${ddt(' + data[0][y] + ')}"',
#                                                       str(data[x][y]))
#             else:
#                 tmp = tmp.replace("${ddt(" + data[0][y] + ")}",
#                                                       str(data[x][y]))
#         case_list.append(tmp)
#     return case_list


# 读取测试用例的yaml
def read_testcase_yaml(yaml_path):
    with open(basicurl() + yaml_path, encoding='utf-8') as f:
        caseinfo = yaml.load(f, Loader=yaml.FullLoader)
        print(caseinfo)
        if len(caseinfo) >= 2:
            return caseinfo
        else:
            if "parameterize" in dict(*caseinfo).keys():
                new_caseinfo = ddt(*caseinfo)

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
            data_list = read_data_yaml(param_value)
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
    # read_case('/testcases/weixin_cs.yml')
    # read_testcase_yaml('/testcases/weixin_cs.yml')
    print(read_testcase_yaml('/testcases/weixin_model/weixin_cs.yml'))
