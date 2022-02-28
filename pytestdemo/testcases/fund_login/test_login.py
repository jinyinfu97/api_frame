import requests
import re
import pytest

from pytestdemo.common.csv_pm import read_testcase_csv
from pytestdemo.common.parametrize import read_testcase_yaml
from pytestdemo.common.requests_util import RequestsUtil
from pytestdemo.debug_talk import Debug_talk
from pytestdemo.log.python_logging import logFrame


class TestFundLogin:
    # 用户获取Ctoken
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/fund_login/get_ctoken_data.yaml'))
    def test_get_ctoken(self, caseinfo):
        res = RequestsUtil(Debug_talk(), 'base_login_url').anylasic_testcase(caseinfo)
        logFrame().logger_info(f'获取Ctoken成功！{res.text}')

    # @pytest.mark.parametrize("caseinfo", read_testcase_csv('/testcases/fund_login/login_data.yaml'))
    # def test_login(self, caseinfo):
    #     res = RequestsUtil(Debug_talk(), 'base_login_url').anylasic_testcase(caseinfo)
    #     logFrame().logger_info(f'用户登录成功！{res.text}')

    # @pytest.mark.repeat(2)
    # 多个用户同时参与活动
    @pytest.mark.parametrize("caseinfo2", read_testcase_yaml('/testcases/fund_login/attend_activity.yaml'))  # 3个参与接口
    @pytest.mark.parametrize("caseinfo1", read_testcase_csv('/testcases/fund_login/login_data.yaml'))  # 2个用户
    def test_attend_activity(self, caseinfo1, caseinfo2):
        RequestsUtil(Debug_talk(), 'base_login_url').anylasic_testcase(caseinfo1)
        RequestsUtil(Debug_talk(), 'base_activity_url').anylasic_testcase(caseinfo2)

    # logFrame().logger_info(f'成功！{res.text}')
