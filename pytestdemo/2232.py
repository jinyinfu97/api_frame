# import jsonpath
# obj= {'headers1':'123'}
# print(type(obj))
# print(jsonpath.jsonpath(obj,'$..headers'))
import json

import jsonpath

from pytestdemo.common.read_config_file import read_data

# for i in range(1,10):
#     for n in range(1,10):
#         if i!=n:
#             print(i,n)
'''
5、用Python开发程序自动计算方案
# 公鸡5文钱一只， 母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱？
'''

# for gj in range(1,101):
#     for mj in range(1,101):
#         for xj  in range(1,101):
#             if (gj + mj + xj == 100):
#                 if gj * 5 + mj * 3 + xj / 3 == 100:
#                     print(f'公鸡、母鸡和小鸡分别为{gj, mj, xj}')

data = {1:2,2:3}
datatype =type(data)
if isinstance(data, list) or isinstance(data, dict):
    print(66666)

