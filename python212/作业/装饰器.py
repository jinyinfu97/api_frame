import time


def runtime(fuc):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            time.sleep(1)
            fuc(*args, **kwargs)
            end_time = time.time()
            cost = str(end_time - start_time)
        except Exception as erro:
            print("错误原因为：", str(erro))
        finally:
            print("打印日志啦！")
            print(f"消耗时间为：{cost}")

    return wrapper


@runtime
def fun1():
    print("我是函数1")



@runtime
def fun2(a,b):
    print("我是函数2")
    print(a+b)


@runtime
def fun3(a,b,*args,**kwargs):
    print("我是函数3")
    print(a+b)

fun1()
fun2(1,2)
fun2([1,2],[3,4])
fun3([1,2],[3,4])