# -*- coding=utf-8 -*-
# @time:2021/10/28
# @phone:15874198829
# @author:码尚教育_星瑶
"""
一、正则表达式
正则表达式的作用：处理文本，提取信息

二、正则表达式如何写？
    1、正则表达式验证工具： https://regex101.com/
    2、正则表达式=普通字符+特殊字符
    普通字符：可以是需要匹配的任意字符，直接匹配
    特殊字符：有特殊函数
三、常见的特殊符号
    .  匹配除换行符之后的任意单个字符
    * 匹配前面的子表达式任意次（包括0次）
    + 匹配前面的子表达式任一次或者多次
    {m,n} 匹配m~n次
    ？ 尽可能少的去匹配
    \  进行转义  如果需要匹配一些特殊字符，就需要用到\进行转义
    \d 匹配0-9之间任意数字符 [0-9]
    \D 匹配不是0-9之间任意数字符 [^0-9]
    \s 匹配任意一个空白字符 包括空格 换行符  tab
    \S 匹配任意不是一个空白字符
    \w 匹配任意一个文字字符 包括字母 数字 下划线
    \W 匹配任意不是文字字符 包括字母 数字 下划线
    []是匹配几个字符之一
    ^ 表示文本开头位置    非
    $  表示文本结尾位置
    ()

三、用正则表达式进行切割字符串


"""
content="""
自动化测试 中科创达软件 9-14K 北京·海淀区·西北旺
自动化测试 龙岩立汇 10-11K 北京·朝阳区·百子湾
自动化测试 凯捷 18-24K·14薪 北京·朝阳区·望京
自动化测试 捷科智诚 11-16K 北京·海淀区·西北旺
自动化测试 理想汽车 15-25K·14薪 北京·顺义区·马坡
自动化测试 博彦科技 16-23K 北京·海淀区·西北旺
自动化测试 先进数通 12-17K 北京·西城区·广安门
自动化测试 东软集团 16-19K·13薪 北京·朝阳区·望京
自动化测试 宇信科技 12-23K·13薪 北京·西城区·金融街
自动化测试 京北方 14-19K 北京·海淀区·西北旺
自动化测试 中科创达软件 11-18K·13薪 北京·海淀区·马连洼
自动化测试 Cognizant 13-24K·13薪 北京·朝阳区·望京
自动化测试 云次方 5-9K 北京
自动化测试 华为 16-24K 北京·海淀区·西北旺
自动化测试 千里马招标网 12-15K·14薪 北京·海淀区·上地
自动化测试 贵州黔菇凉科技有... 12-13K 北京·丰台区·科技园区
自动化测试 三一重工 20-40K·16薪 北京·昌平区·二拨子村
自动化测试 易申日用品经销部 30-55K 北京·海淀区·知春路
自动化测试 中软国际 10-15K 北京·海淀区·四季青
自动化测试 微创软件 15-20K 北京·朝阳区·望京
自动化测试工程师 天阳科技 11-17K 北京·东城区·安定门
自动化测试 中信银行 30-35K 北京·朝阳区·高碑店
自动化测试 博彦科技 16-20K·13薪 北京·海淀区·西北旺
自动化测试 中电金信 11-18K 北京·丰台区·科技园区
自动化测试 中科创达软件 8-13K 北京·海淀区·西北旺
自动化测试 建信融通 15-30K 北京·西城区·广安门
自动化测试 京北方信息 11-20K 北京·海淀区·魏公村
自动化测试 理想汽车 20-40K·14薪 北京·顺义区·马坡
自动化测试 千里马招标网 12-15K·14薪 北京·海淀区·上地
自动化测试开发工程师 Cerence 15-20K 北京·朝阳区·酒仙桥
"""

"""
方案一：通过string的内置函数来处理  join  split  find  isdigit。。。。
"""
lines=content.splitlines()
for line in lines:
    index0 = 0
    for n in range(len(line)-1):
        if line[n]==' ' and line[n+1].isdigit()==True:
            index0 = index0+n
        elif line[n]=='K' and line[n+1]==' ':
            print(line[index0+1:n+1])
        elif line[n]=='·' and line[n+1].isdigit()==True:
            pos2 = line.find('薪')
            print(line[index0+1:pos2+1])





    # pos2=line.find('薪')
    # print(pos2,line[0:pos2])


# for line in lines:
#     pos2=line.find('薪')
#     if pos2<0:
#         pos2 = line.find('K')
#         if pos2<0:
#             continue
#     index=pos2-1
#
#     while line[index].isdigit()or line[index]=='-'or line[index]=='·'or line[index]=='K':
#         index-=1
#     pos1=index+1
#
#     print(line[pos1:pos2+1])

"""
方案二：正则表达式来写
"""
import re
r=re.compile(r'\d+-\d+K[·\d薪]*')
for one in r.findall(content):
    print(one)


content2="""15874198829我的手机号码1111
15911111111我的手机号码1111
13511111111我的手机号码1111
15711111111我的手机号码1111
"""
import re
# (\d+)我的手机号码(\d+)
r=re.compile(r'(\d+)我的手机号码(\d+)')
for one in r.findall(content2):
    print(one)

"""字符串切割"""
content3='MS234;叶落知秋 MS235,MS236'
# print(content3.split(';'))
names=re.split(r'\W+',content3)
print(names)