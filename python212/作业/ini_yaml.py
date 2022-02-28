'''
1、熟练ini文件编写格式、ini文件字节\选项\选项值读取、及字节\选项\选项值的编辑
2、yaml各种数据类型编辑格式
3、封装函数，如何实现yaml文件保存为内存数据？
4、封装函数内存数据如何通过yaml文件进行存储？
'''
import configparser

import yaml


def read_ini(filename):
    config = configparser.ConfigParser()
    # 字节读取
    with open(filename, encoding='utf-8') as f:
        config.read(filename,encoding='utf-8')
        s = config.sections()
        print(s)
    #选项读取
        for i in s:
            option = config.options(i)
            print(f'{i}节点下的选项是{option}')
    #选项值读取
            for n in option:
                value = config.get(i,n)
                print(f'{i}节点下的{n}的选项的选项值为{value}')
def edit_ini(filename):
    config = configparser.ConfigParser()
    config.read(filename, encoding='utf-8')
    # 增加节点
    config.add_section('path')
    # 字节的编辑
    config.set('userinfo', 'salary', '20000')
    with open(filename,mode='w+',encoding='utf-8') as f:
        config.write(f)

def write_yaml(filename):
    info2 = {'id':123,"method":"get",'lg':['中文','英文','法文']}
    with open(filename, mode='a+', encoding='utf-8') as f:
        yaml.dump(info2,stream=f,allow_unicode=True,encoding="utf-8")
def read_yaml(filename):
    with open(filename, mode='r+', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        print(value)











if __name__ == '__main__':
    # edit_ini('file.ini')
    # read_ini('file.ini')
    # write_yaml('file.yaml')
    read_yaml('../../httrunner_teat/weixin_test.yml')

