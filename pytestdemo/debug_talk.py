import hashlib
import random
import time

from pytestdemo.common.read_config_file import read_data


class Debug_talk:
    def get_random_num(self, min, max):
        return str(random.randint(int(min), int(max)))

    def get_extra_data(self, data):
        return read_data(data)

    def get_int(self, data):
        return int(data)

    def update_extra_data(self,token,id):

        return str(token+'&'+self.get_extra_data(id))

    # MD5加密
    def md5(self, args):
        # 以指定的编码格式编码字符串
        utf8_str = str(args).encode("utf-8")
        # md5加密（哈希算法）
        md5_str = hashlib.md5(utf8_str).hexdigest()
        return md5_str.lower()

if __name__ == '__main__':
    print(Debug_talk().md5("yy1234qwer"))