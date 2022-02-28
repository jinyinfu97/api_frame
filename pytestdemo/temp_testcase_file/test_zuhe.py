import requests
import re
import pytest

from pytestdemo.common.requests_util import RequestsUtil


def test_select_zuhe():
    url = 'http://fundtest.eastmoney.com/zktfavor/MonthMailReport/getzhlist'
    res = requests.request('get', url=url)
    # print(res.json())
    zhlist = []
    for i in res.json()['Data']:
        zhlist.append(i['ZHCODE'])
    return zhlist


huobizh = []
@pytest.mark.parametrize("zhcode", test_select_zuhe())
def test_zu_info(zhcode):
    url = 'https://jijinbaapi.eastmoney.com/FundMCApi/FundMBNew/FZH15DynamicPostList2'

    headers = {
                "Host": "jijinbaapi.eastmoney.com",
                "Accept": "*/*",
                "GTOKEN": "C59338F8EE684BB2A6E01353457F31be",
                "clientInfo": "ttjj-iPhone11,8-iOS-iOS14.6",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "EMProjJijin/6.4.8 (iPhone; iOS 14.6; Scale/2.00)",
                "Connection": "keep-alive",
                "Referer": "https://mpservice.com/a461099f332046f0b32783c5d3d980a8/release/pages/index/index"

            }
    data = {
                    "ApiType": "4",
                    "CToken": "",
                    "CustomerNo": "",
                    "MobileKey": "ACE87AB5-50F8-48B7-A2AF-51B043BEB8D7",
                    "Passportid": "",
                    "PhoneType": "IOS14.6.0",
                    "ServerVersion": "6.4.8",
                    "TimePoint": "0",
                    "UToken": "",
                    "UserId": "",
                    "ZHCode": zhcode,
                    "appVersion": "6.4.8",
                    "customerNo": "",
                    "deviceid": "ACE87AB5-50F8-48B7-A2AF-51B043BEB8D7",
                    "pageSize": "1",
                    "plat": "Iphone",
                    "product": "EFund",
                    "version": "6.4.8",
                }
    res = requests.request('post', url=url,data=data,headers=headers)
    for i in res.json()['Data'][0]['warehouseRecord']['CombDetailList']:
        if i['TargetProp']!="0.0" and i['ClassifyName']=='货币型':
            huobizh.append(res.json()['Data'][0]['warehouseRecord']['SubAccountNo'])
    print(huobizh)







