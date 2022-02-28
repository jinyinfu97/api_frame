import requests
import re
import pytest

#获取所有投顾
def test_seltg():
    url = 'http://fundtest.eastmoney.com/zktfavor/tougu/gettougulist'

    res = requests.request('get',url=url)
    tglist = []
    for i in res.json()['Data']:
        tglist.append(i['Code'])
    return tglist

#验证投顾是否都包含相应字段
@pytest.mark.parametrize("tgcode", test_seltg())

def test_TGcontain(tgcode):
    ziduan = []
    url = 'https://uni-fundts.1234567.com.cn/dataapi/IAAGGR/FundIATGInfoAggr'
    parmars ={
        'TGCODE':tgcode,
        'FIELDS':'SYL_Z,SYL_Y,SYL_3Y,SYL_6Y,SYL_1N,SYL_2N,SYL_3N,SYL_5N,SYL_JN,ANNSYL_LN'
    }
    res = requests.get(url=url,params=parmars)
    for x, y in res.json()['data'][0].items():
        ziduan.append(x)
    for m in ["SYL_Z","SYL_Y","SYL_3Y","SYL_6Y","SYL_1N","SYL_2N","SYL_3N","SYL_5N","SYL_JN","ANNSYL_LN"]:
        if m in ziduan:
            assert 1==1
        else:
            assert 1==2

