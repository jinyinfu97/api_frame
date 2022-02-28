# _*_ coding:utf-8 _*-
# 作者：码尚学院_星瑶老师
# @Time: 2021/5/10
# @Email:2155896749@qq.com
# @File: log.py

import logging
class FrameLog:
    def getLogger(self):
        # 创建日志器
        logger = logging.getLogger("logger")
        # 日志输出当前级别及以上级别的信息,默认日志输出最低级别是warning
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            # 创建控制台处理器----》输出控制台
            SH = logging.StreamHandler()
            # 创建文件处理器----》输出文件
            FH = logging.FileHandler("log.txt")
            # 日志包含哪些内容    时间  文件  日志级别 ：事件描述/问题描述
            formatter = logging.Formatter(fmt="[%(asctime)s] [%(filename)s] %(levelname)s :%(message)s",
                                          datefmt='%Y/%m/%d %H:%M:%S')
            logger.addHandler(SH)
            logger.addHandler(FH)
            SH.setFormatter(formatter)
            FH.setFormatter(formatter)

        return logger

    def sum(self,*args):
        """
        求多个数之和
        :param args:
        :return:
        """
        try:
            sum=0
            for num in args:
                sum+=num

            self.getLogger().info(f"计算多个数之和={sum}")
            return sum
        except  Exception as  error:
            self.getLogger().error("计算多个数之和有异常:\n"+str(error))


    def sum_two(self,x,y):
        """
        求两个数之和
        :param args:
        :return:
        """
        try:
            sum=0
            sum=x+y
            self.getLogger().info(f"计算多个数之和={sum}")
            return sum
        except  Exception as  error:
            self.getLogger().error("计算多个数之和有异常:\n"+str(error))

    def sum_three(self,x,y,z):
        """
        求两个数之和
        :param args:
        :return:
        """
        try:
            sum=0
            sum=x+y+z
            self.getLogger().info(f"计算多个数之和={sum}")
            return sum
        except  Exception as  error:
            self.getLogger().error("计算多个数之和有异常:\n"+str(error))
# 常见一个问题
if __name__ == '__main__':
    # logger添加一个文件处理器和一个控制台处理器
    FrameLog().sum(1,2,3)
    # logger添加2个文件处理器和2个控制台处理器
    FrameLog().sum_two(1, 2)
    # logger添加3个文件处理器和3个控制台处理器
    FrameLog().sum_three(1, 2,3)




