import hashlib
import hmac
import json
import random
import string
from functools import wraps
from flask import Flask, make_response, request

#基于Flask框架的Mock Server接口文件

SECRET_KEY = "DebugTalk"
app = Flask(__name__)
users_dict = {}
token_dict = {}

#返回指定长度str_len的随机字符串
def gen_random_string(str_len):
    """
    string.ascii_letters返回字符串：abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    string.digits返回字符串：0123456789
    random.choice(列表/元祖/字符串)返回一个列表/元祖/字符串其中的随机一个值。
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))


print(gen_random_string(123))


#返回经过秘钥签名加密之后的字符串
def get_sign(*args):
    """
    encode()将字符串转换成bytes类型
    hmac:hex-based message authentication code 哈希消息认证码
    hmac.new(key,msg,digestmod) 以一个密钥和一个消息为输入，利用哈希算法，生成一个消息摘要作为输出!
    #key是密钥(bytes类型)，msg是待加密的字符串(bytes类型)，digestmod是hash函数，
    hexdigest() #打印出加密后字符串的十六进制格式
    digest()    #打印出字符串的ascii格式
    """
    sign_key = SECRET_KEY.encode('ascii')
    content = ''.join(args).encode('ascii')
    sign = hmac.new(sign_key,content,hashlib.sha1).hexdigest()
    return sign

#返回经过MD5加密之后的字符串
def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()

#验证请求
def validate_request(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        device_sn = request.headers.get('device_sn', "")
        token = request.headers.get('token', "")

        if not device_sn or not token:
            result = {
                'success': False,
                'msg': "device_sn or token is null."
            }
            response = make_response(json.dumps(result), 401)
            response.headers["Content-Type"] = "application/json"
            return response

        if token_dict.get(device_sn) != token:
            result = {
                'success': False,
                'msg': "Authorization failed!"
            }
            response = make_response(json.dumps(result), 403)
            response.headers["Content-Type"] = "application/json"
            return response

        return func(*args, **kwargs)

    return wrapper

#自定义接口：POST请求，data传参
@app.route('/get_token', methods=["GET"])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    print(request.headers)
    print(username,password)
    if username==str(gen_md5('admin')).upper() and password==str(gen_md5('123')).upper():
        return {'error_code':'0','message':'登录成功','data':[{'api_token':gen_md5('admin123')}]}
    else:
        return {'error_code':'-1','message':'参数有误','data':[]}

# if __name__ == '__main__':
#     app.run()