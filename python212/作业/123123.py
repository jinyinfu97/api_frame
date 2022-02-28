import time


def fun():
    start_time = time.time()
    print("kaishila")
    time.sleep(1)
    end = time.time()
    cost = end-start_time
    print(f"消耗时间为：{cost}")
fun()