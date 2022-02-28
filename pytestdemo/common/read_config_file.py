import csv

import yaml
import os


def basicurl():
    return os.getcwd().split('common')[0]


# 读取config.yaml
def read_config_yaml(one_node, two_node):
    with open(basicurl() + "/config/config.yml", encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value[one_node][two_node]


# def read_yaml(num):
#     with open(basicurl()+'\\config\\config.yml', mode='r+', encoding='utf-8') as f:
#         value = yaml.load(stream=f, Loader=yaml.FullLoader)
#         return value[num]['url']
def read_data(token):
    with open(basicurl() + '\\testcases\\extract.yml', mode='r+', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[token]


def read_all_data():
    with open(basicurl() + '\\testcases\\extract.yml', mode='r+', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


def clean_data():
    with open(basicurl() + '\\testcases\\extract.yml', mode='w', encoding='utf-8') as f:
        f.truncate()


def write_extract(data):
    with open(basicurl() + '\\testcases\\extract.yml', mode='a', encoding='utf-8') as f:
        # case_data = read_all_data()
        # for data_key, data_value in dict(data).items():
        #     _data_key = data_key
        #     _data_value = data_value
        # if case_data:
        #     for case_key, case_value in case_data.items():
        #         if case_key == _data_key:
        #             _data_key = str(case_key) + "1"
        #             data = {_data_key: _data_value}
        #     yaml.dump(data=data, stream=f, allow_unicode=True, encoding="utf-8")
        # else:
        yaml.dump(data=data, stream=f, allow_unicode=True, encoding="utf-8")
        # return data


class DataHandle:
    str_lis = []
    int_in_data = []

    # 获取字符串中的整数
    def get_num_in_data(self, data: str):
        if self.contain_num(data):
            start_index = data.index(self.int_in_data[0])
            end_index = data.index(self.int_in_data[-1])
            return int(data[start_index:end_index + 1])

    # 判断字符串中是否包含整数
    def contain_num(self, data: str):
        num_lis = [_ for _ in range(0, 10)]

        for _ in num_lis:
            self.str_lis.append(str(_))
        for _ in data:
            if _ in self.str_lis:
                self.int_in_data.append(_)
        for _ in data:
            if _ in self.str_lis:
                return True


# 读取数据的yaml
def read_data_yaml(yaml_path):
    with open(basicurl() + yaml_path, encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


def read_csv_data(csv_path):
    with open(basicurl() + csv_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        return rows


if __name__ == '__main__':
    print(read_all_data())
    print(write_extract({'CustomerNo': '82a11be5330dec4cc99edfaae8de997226'}))
