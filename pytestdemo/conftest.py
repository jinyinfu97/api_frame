import random

import pytest

from pytestdemo.common.read_config_file import clean_data, write_extract
from pytestdemo.common.requests_util import RequestsUtil
from pytestdemo.debug_talk import Debug_talk
from pytestdemo.log.python_logging import logFrame


@pytest.fixture(scope="session", autouse=True)
def clean_all_data():
    clean_data()



# @pytest.fixture(scope="session",autouse=True)
# def get_token(caseinfo):
# 	# url = "/token"
# 	# data = {
# 	# 	"grant_type": "client_credential",
# 	# 	"appid": "wxac9525af0278fe45",
# 	# 	"secret": "f12e101c5b159d22c60b8a39cf5bf673"
# 	# }
# 	res = RequestsUtil().anylasic_testcase(caseinfo)
# 	# res = RequestsUtil().send_requests(2,'get', url=url, params=data)
# 	data = {"access_token":res.json()['access_token']}
# 	write_data(data)
# 	print('流程开始执行，获取token成功！')
# 	# print(res.json()['access_token'])
# 	yield res.json()['access_token']
# 	print('流程执行完成！')

# @pytest.fixture(scope="function")
# @pytest.mark.parametrize("caseinfo", read_case('\\testcases\\create_tags.yml'))
# def create_tag(caseinfo):
#     res = RequestsUtil(Debug_talk()).anylasic_testcase(caseinfo)
#     logFrame().logger_info(f"执行删除或者编辑标签之前，先创建标签成功并返回结果：{res.text}")


@pytest.fixture(scope="session")
def get_Ctoken():
    headers = {
        "Host": "tradeapineice.1234567.com.cn",
        "Accept": "*/*",
    }
    data = {
        "CToken": "h-1chre-udknkf6nnk--q6e8huhfuerh.1",
        "PhoneType": "Iphone",
        "Version": "6.4.8",
        "ServerVersion": "6.4.8",
        "ReqNo": "2281621467",
        "AppType": "ttjj",
        "DeviceOS": "iOS 15.0.2",
        "MobileKey": "87C7E8F1-4A80-4045-B0DD-443176FFA5D3",
        "GTOKEN": "A641CBFE4352465485D0447C8D51AFe3",
        "MarketChannel": "Appstore",
        "DeviceType": "iPhone13,2",
        "appVersion": "6.4.8",
        "DeviceName": "Xin的iPhone",
    }
    res = RequestsUtil().send_requests(1, 'post', '/GetCToken', headers=headers, json=data)
    if res.json()['Data'] == None:
        raise Exception('参数错误！！！！')
    return res.json()['Data']

# def execute_sql():
# 	print("执行数据库的验证，查询数据库。")
# 	yield
# 	print("关闭数据库的连接")
