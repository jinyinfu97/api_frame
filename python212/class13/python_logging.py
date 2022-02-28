# -*- coding=utf-8 -*-
# @time:2021/10/26
# @phone:15874198829
# @author:码尚教育_星瑶
"""
一、什么是日志
    日志：跟踪软件运行时事件的方法（跟踪器）
    日志作用：
    1、调试程序，定位问题
    2、数据分析
    3、用户信息跟踪
二、python如何实现日志收集
    1、python内置模块：logging
    2、logging模块的基本应用
        四大组件：
        1、日志器：logger  给所有的应用程序提供入口
        2、处理器：handler   决定在不同端实现输出
        3、格式器：formater   决定日志内容（日志包含什么样的信息（时间 某行  信息描述  信息级别  ））
        4、过滤器：filter     信息进行筛选，保留感兴趣的信息

        四大组件之间的关系：
        1个日志器可以有多个处理器，一个处理器可以有各自的格式器和过滤器

    3、日志级别
    日志级别哪些，优先级从低到高分别有哪些？
     DEBUG:调试信息
     INFO：关键事件描述
     WARNING：警告信息
     ERROR：错误信息
     CRITICAL：严重错误

    日志输出端：日志文件  控制台

    输出日志级别由日志输出级别和处理器输出级别控制

    输出日志级别先按照日志器级别再按照处理器级别实现日志输出

# 问题1：asctime和filename是可以自己命名的对吧  ?
问题2：处理器已经设置了级别,日志器又设置级别 ,处理器的就不生效了是吧  ？？？？

"""

import logging

# 创建一个日志器
import time


class logFrame:

    def getlogger(self):
        self.logger = logging.getLogger("logger")
        if not self.logger.handlers:
            # 日志输出默认级别Warning及以上级别信息
            self.logger.setLevel(logging.DEBUG)
            # 创建一个处理器  StreamHandler()控制台实现日志输出
            sh = logging.StreamHandler()
            # 创建一个格式器（日志内容：时间 文件 日志级别  日志描述信息）
            # 问题1：asctime和filename是可以自己命名的对吧  ?
            formatter = logging.Formatter(fmt="%(asctime)s | %(filename)s(%(lineno)d 行) | %(levelname)s| %(message)s",
                                          datefmt="%Y/%m/%d %H:%M:%S")

            # 创建一个处理器  文件处理器 文件写入日志
            fh = logging.FileHandler(filename="{}_log.txt".format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())),
                                     encoding="utf-8")
            formatter2 = logging.Formatter(fmt="%(asctime)s | %(filename)s:%(lineno)d| %(levelname)s| %(message)s",
                                           datefmt="%Y/%m/%d %H:%M:%S")
            self.logger.addHandler(sh)
            sh.setFormatter(formatter2)
            # sh.setLevel(logging.INFO)

            self.logger.addHandler(fh)
            fh.setFormatter(formatter)

        return self.logger

    def logger_debug(self, msg, *args, **kwargs):
        self.logger = logFrame().getlogger()
        return self.logger.debug(msg, *args, **kwargs)

    def logger_info(self, msg, *args, **kwargs):
        self.logger = logFrame().getlogger()
        return self.logger.info(msg, *args, **kwargs)

    def logger_error(self, msg, *args, **kwargs):
        self.logger = logFrame().getlogger()
        return self.logger.error(msg, *args, **kwargs)

    def logger_critical(self, msg, *args, **kwargs):
        self.logger = logFrame().getlogger()
        return self.logger.critical(msg, *args, **kwargs)


if __name__ == '__main__':
    # 输出日志
    log = logFrame()
    logger = log.getlogger()

    try:
        num = int(input("输入一个除数："))
        sum = 4 / num
        logFrame().logger_info(f"4/{num}={sum},计算完成！")
        # logger.info(f"4/2={sum},计算完成！")
        # logger.debug("debug信息")
        logFrame().logger_debug('调试信息---------------------')
    except Exception as error:
        logFrame().logger_error(f'错误信息为{error}')

    logger.info("bbb")
    logger.info("ccc")



