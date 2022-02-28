#MD5加密
import base64
import hashlib


def md5(args):
    return hashlib.md5(str(args).encode('utf-8')).hexdigest()
#Base64加密
def bs64(args):
    return base64.b64encode(str(args).encode("utf-8")).decode(encoding ="utf-8")

print(bs64('admin').upper())
print(bs64("123").upper())