# NOTE: Generated By HttpRunner v3.1.6
# FROM: weixin_test.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseWeixinTest(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/cgi-bin/token")
            .get("https://api.weixin.qq.com/cgi-bin/token")
            .with_params(
                **{
                    "appid": "wxac9525af0278fe45",
                    "grant_type": "client_credential",
                    "secret": "f12e101c5b159d22c60b8a39cf5bf673",
                }
            )
            .with_headers(
                **{
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Host": "api.weixin.qq.com",
                    "Postman-Token": "b7a29129-f395-479b-b425-c2ff99ca5e41",
                    "User-Agent": "PostmanRuntime/7.28.4",
                }
            )
            .extract()
            .with_jmespath("body.access_token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; encoding=utf-8")
            .assert_equal("body.expires_in", 7200)
        ),
        Step(
            RunRequest("/cgi-bin/tags/get")
            .get("https://api.weixin.qq.com/cgi-bin/tags/get")
            .with_params(**{"access_token": "$token"})
            .with_headers(
                **{
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Length": "2",
                    "Content-Type": "text/plain",
                    "Host": "api.weixin.qq.com",
                    "Postman-Token": "d5b860cf-5e86-4eca-86cd-39bfd902c09f",
                    "User-Agent": "PostmanRuntime/7.28.4",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; encoding=utf-8")
        ),
        Step(
            RunRequest("/cgi-bin/tags/create")
            .post("https://api.weixin.qq.com/cgi-bin/tags/create")
            .with_params(
                **{
                    "access_token": "50_nAlB3-NyrFo6FgGlRqFFK4TjG4fZlQTQGXNSMcivD6MXzW0icTYTHo71Qfna5WUfbogOC6YlUp3k6OgUOmGNUtTLSZaCSOZqS1RF2zXoXy4FWYuC8PmEyQkbq3puD2gTTYiyMndxxSSDA9f2RUZeABAZCH"
                }
            )
            .with_headers(
                **{
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Length": "26",
                    "Content-Type": "application/json",
                    "Host": "api.weixin.qq.com",
                    "Postman-Token": "2639cc83-ada2-4a69-b090-e7e995321f87",
                    "User-Agent": "PostmanRuntime/7.28.4",
                }
            )
            .with_json({"tag": {"name": "苏州"}})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; encoding=utf-8")
        ),
    ]


if __name__ == "__main__":
    TestCaseWeixinTest().test_start()