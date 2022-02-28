import requests
import re
import pytest
from  pytestdemo.common.requests_util import RequestsUtil
def test_getActiveInfo():

    headers = {
                    "Host": "actsl-test.1234567.com.cn",
                    "Accept": "application/json, text/plain, */*",
                    "Connection": "keep-alive",
                    "Cookie": "st_asi=20211026110316651-119310318487-5628458986-ttdntlty.syz.cygfan2.click-1; st_inirUrl=; st_psi=20211026110316651-119310318487-5628458986; st_pvi=02783806063656; st_sn=8; st_sp=2021-10-26%2011%3A02%3A47; st_si=58357791788837",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8 (__WKWebView__) ttjj/6.4.8",
                    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
                    "Referer": "https://actsl-test.1234567.com.cn/topic/2021/bellwether-activity/pages/index/index?zone=12&uid=5ffa0fcb465e4ab1b316f2eaa6e36b91&version=6.4.8&plat=Iphone&product=EFund&platid=1&hybridzone=12&terminal=true&appType=ttjj&fromPlat=1&showNavbar=0&fromWhere=native&v=6.4.8&isapp=1",
                    "Accept-Encoding": "gzip, deflate, br",
                }
    params = {
            "activeid": "A20210719162742",
            "userid": "5ffa0fcb465e4ab1b316f2eaa6e36b91",
            "ctoken": "rnud8-hahu8daeq6qfqq11c8uhreadhh.12",
            "utoken": "fkkuu6d-jaud8hfck-66188a6eqdjdkcc1f5aa46.12",
            "gtoken": "A641CBFE4352465485D0447C8D51AFe3",
            "deviceid": "87C7E8F1-4A80-4045-B0DD-443176FFA5D3",
            "passportid": "1860114714251838",
            "version": "648",
        }
    cookies ={
                    "st_asi": "20211026110316651-119310318487-5628458986-ttdntlty.syz.cygfan2.click-1",
                    "st_inirUrl": "",
                    "st_psi": "20211026110316651-119310318487-5628458986",
                    "st_pvi": "02783806063656",
                    "st_sn": "8",
                    "st_sp": "2021-10-26%2011%3A02%3A47",
                    "st_si": "58357791788837",
                }
    res = RequestsUtil().send_requests(0,'get','/getActiveInfo',headers=headers,params=params,cookies=cookies)
    print(res.json())