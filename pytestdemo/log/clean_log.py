import os


# 该函数用于删除文件
# 默认路径：C:\Users\Administrator\PycharmProjects\pythonProject4\pytestdemo\log
def scan(dirname=r'C:\Users\Administrator\PycharmProjects\pythonProject4\pytestdemo\log'):
    # 提示用户输入目录路径
    if os.path.exists(dirname) == False:  # 检查用户输入的目录是否存在，如果不存在则退出程序
        print("输入的目录不存在！")
    else:

        filename = os.listdir(os.getcwd())
        for file in filename:
            if file[-7:] == "log.txt":
                print("删除文件：", file)
                file = dirname + "\\" + file
                os.remove(file)
                print(f"成功删除{file}!")


scan()
