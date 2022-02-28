import requests
import pytest
from pytestdemo.temp_testcase_file.test_zuhe import test_select_zuhe

#验证活期组合是否不含有成立来年化



def test_Hqzh():
    url = 'https://uni-fundts.1234567.com.cn/dataapi/subAccount/getSecondPageSubAccountMarketingData?combineCodeList=10198717%2C10695897%2C10326645&extraRisk=Z1&pageNum=1&pageSize=1000'
    headers = {
        "Host": "uni-fundts.1234567.com.cn",
        "Accept": "*/*",
        "GTOKEN": "C59338F8EE684BB2A6E01353457F31be",
        "clientInfo": "ttjj-iPhone11,8-iOS-iOS14.6",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "EMProjJijin/6.4.8 (iPhone; iOS 14.6; Scale/2.00)",
        "Connection": "keep-alive",
        "Referer": "https://mpservice.com/8fab06f8d939415584f2ce3a28846b5f/release/pages/subListPage/index"

    }
    res = requests.request('get',url=url,headers=headers)
    zhlist = []
    for i in res.json()['Data']['mainCombineCombineList']:
        zhlist.append(i['combineCode'])
    return zhlist



def test_01():
    # 获取非活钱组合列表
    fhzh = test_select_zuhe()
    for a in test_Hqzh():
        fhzh.remove(a)
    return fhzh
    # print(fhzh)

errozh = []
Nzh = []
@pytest.mark.parametrize("zhcode", test_01())#非活钱组合参数
# @pytest.mark.parametrize("zhcode", test_Hqzh())#活钱组合参数
def test_zhSY(zhcode):
    ziduan = []
    url = 'https://h5test.1234567.com.cn/AggregationStaticService/chooseCustomRouter/getComboBagBaseInfoAggr'
    headers = {
        "Host": "h5test.1234567.com.cn",
        "Origin": "https://materialtest.1234567.com.cn",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Referer": "https://materialtest.1234567.com.cn/render/616d3c94f08d730735c4ce54/index.html?debug=true&spm=fund&zone=&uid=&version=6.4.9&plat=Iphone&product=EFund&platid=1&hybridzone=&terminal=true&appType=ttjj&fromPlat=1&showNavbar=0&fromWhere=native&v=6.4.9&isapp=1"

    }
    params = {
        "subAccountNo":zhcode
    }
    res = requests.get(url=url,params=params,headers=headers)

    for n in res.json()['data'][0]['intervalList']:
        ziduan.append(n['intervalType'])
        # if n['intervalType'] == 'LJJZ' and n['intervalRate'] == 0:
        #     errozh.append(zhcode)
        # elif n['intervalType'] == 'NH_1M' and n['intervalRate'] == 0:
        #     errozh.append(zhcode)
        if n['intervalType'] == 'SYL_1N' and n['intervalRate'] == 0:
            errozh.append(zhcode)
            # Nzh.append(n['intervalRate'])

    # return Nzh
    print(errozh)
    # 非活钱组合收益验证
    # if ziduan ==['SYL_Z','SYL_Y','SYL_3Y','SYL_6Y','SYL_1N','SYL_LN','SE']:
    #     assert 1==1
    #
    # else:
    #     errozh.append(zhcode)
    #     assert 1==2
    # print(errozh)



    #活钱组合收益验证
    # if ziduan ==['SYL_Z','SYL_Y','SYL_3Y','SYL_6Y','SYL_1N','SYL_LN','LJJZ','NH_1M']:
    #     assert 1==1
    # else:
    #     errozh.append(zhcode)
    #     assert 1==2
    # print(errozh)


        # if n['intervalType']!='SE':
        #     assert 1==1
        # elif n['intervalType'] =='SYL_Z' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='SYL_Y' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='SYL_Y' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='SYL_6Y' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='SYL_1N' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='SYL_LN' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='LJJZ' and n['intervalRate'] !="--":
        #     assert 1==1
        # elif n['intervalType'] =='NH_1M' and n['intervalRate'] !="--":
        #     assert 1==1
        # else:
        #     errozh.append(zhcode)
        #     assert 1==2
    # print(errozh)
if __name__ == '__main__':
    pytest.main()

