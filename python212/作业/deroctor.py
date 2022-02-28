import time

from python212.class13.python_logging import logFrame


def logging(func):
    def wrapper(*args, **kwargs):
        logFrame().logger_info('开始记录执行开始时间-------')
        try:
            start_time = time.time()
            time.sleep(1)
            messge=func(*args, **kwargs)
            end_time = time.time()
            cost = end_time - start_time
            logFrame().logger_info(f'{func.__name__}执行一共花费{cost - 1}秒-------')
            logFrame().logger_info(f'{func.__name__}函数执行结果为{messge}')
        except Exception as erro:
            logFrame().logger_error(f'执行{func.__name__}函数过程中出错，错误原因为{erro}')

    return wrapper

@logging
def fun1(a, b):
    print(f'{a}+{b}={a + b}')
    return a+b

@logging
def fun2(a, b):
    print(f'{a}*{b}={a * b}')
    return a * b

    # raise Exception('自己加的报错！！')
@logging
def fun3(a, b):
    print(f'{a}*{b}={a * b}')
    return a * b

fun1(1,2)
fun2(3,4)
fun3('1','2')

