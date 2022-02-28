# -*- coding=utf-8 -*-
# @time:2021/10/26
# @phone:15874198829
# @author:码尚教育_星瑶
from python_logging import logFrame
import logging

# 创建一个日志器
import time


def test():
    logger=logFrame().getlogger()
    logger.info("11111")

def test2():
    logger=logFrame().getlogger()
    logger.info("22222")

def test3():
    logger=logFrame().getlogger()
    logger.info("333")

def test4():
    logger=logFrame().getlogger()
    logger.info("4444")

if __name__ == '__main__':
    test()
    test2()
    test3()
    test4()
