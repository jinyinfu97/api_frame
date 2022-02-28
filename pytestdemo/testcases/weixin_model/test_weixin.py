# encoding:utf-8
import pytest

from pytestdemo.common.csv_pm import read_testcase_csv
from pytestdemo.common.parametrize import read_testcase_yaml
from pytestdemo.common.requests_util import RequestsUtil
from pytestdemo.debug_talk import Debug_talk
from pytestdemo.log.python_logging import logFrame



class TestWeiXin:
    list1 = []

    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/weixin_model/weixin_cs.yml'))
    # def test_get_token(self, caseinfo):
    #     res = RequestsUtil(Debug_talk(), 'base_wxgl_url').anylasic_testcase(caseinfo)
    #     logFrame().logger_info(f'获取token成功！{res.text}')

    # 获取公众号已创建的标签接口

    @pytest.mark.parametrize("caseinfo2", read_testcase_yaml(r'\testcases\weixin_model\get_all_data.yml'))
    @pytest.mark.parametrize("caseinfo1", read_testcase_yaml(r'\testcases\weixin_model\weixin_cs.yml'))
    def test_get_tags(self, caseinfo1, caseinfo2):
        RequestsUtil(Debug_talk(), 'base_wxgl_url').anylasic_testcase(caseinfo1)
        RequestsUtil(Debug_talk(), 'base_wxgl_url').anylasic_testcase(caseinfo2)
        # logFrame().logger_info(f"获取所有标签成功！：{res.text}")
        # for n in range(len(res.json()['tags'])):
        #     id = res.json()['tags'][n]['id']
        #     TestApi02.list1.append(id)
        # write_extract({"i":TestApi02.list1})

    # # 创建标签接口
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/weixin_model/create_tags.yml'))
    # def test_create_tag(self, caseinfo):
    #     res = RequestsUtil(Debug_talk(), 'base_wxgl_url').anylasic_testcase(caseinfo)
    #     logFrame().logger_info(f"创建标签成功并返回结果：{res.text}")
    #
    # # 编辑标签接口
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/weixin_model/update_tags.yml'))
    # def test_edit_tag(self, caseinfo):
    #     res = RequestsUtil(Debug_talk(), 'base_wxgl_url').anylasic_testcase(caseinfo)
    #     logFrame().logger_info(f"编辑标签成功并返回结果：{res.text}")
    #
    # # 删除所有标签
    # @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/weixin_model/delete_tags.yml'))
    # def test_delete_all_tag(self, caseinfo):
    #     res = RequestsUtil(Debug_talk(), 'base_wxgl_url').anylasic_testcase(caseinfo)
    #     logFrame().logger_info(f"删除标签并返回结果：{res.text}")





'''
    #创建标签接口
    @pytest.mark.parametrize("caseinfo", read_case()[2])
    @pytest.mark.parametrize("name",[f"上海{random.randrange(1,1000)}",f"北京{random.randrange(1,1000)}",f"广东{random.randrange(1,1000)}",f"江苏{random.randrange(1,1000)}",f"浙江{random.randrange(1,1000)}"])
    def test_create_tag(self,caseinfo,name):
        # url = '/tags/create?access_token={{access_token}}'
        # headers = {
        #     'Content-Type':'application/json'
        # }
        # data = {"tag":{"name":name}}
        write_data(name)
        res = RequestsUtil().anylasic_testcase(caseinfo)
        # res = RequestsUtil().send_requests(2,'post',url, json=data,headers =headers)
        # res = res.text.encode('unicode_escape').decode('unicode_escape')
        logFrame().logger_info(f"标签{name}添加成功！, 返回结果是：{res.text}")
        # print(f"{name}添加成功！", res.text)
        # assert res.status_code ==200
    
    # 删除标签接口
    def test_delete_tag(self,new_tag):

        url = '/tags/delete?access_token={{access_token}}'
        data = {"tag": {"id": new_tag['id']}}
        res = RequestsUtil().send_requests(2,'post',url, json=data)
        # res.content.decode('unicode_escape')
        logFrame().logger_info(f"删除{new_tag['name']}标签并返回结果：{res.text}")
'''
