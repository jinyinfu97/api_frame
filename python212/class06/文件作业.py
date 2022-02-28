# 1、封装读取某个文件，读取指定长度内容，并返回读取的内容
def read_file(filename, num):
    with open(filename, "r+", encoding="utf-8") as f:
        value = f.readline(num)
        return value


# print(read_file("info.txt", 3))

# 2、封装函数读取某个文件的所有行的内容，并把每行的内容作为列表返回
def read_all_lines(filename):
    with open(filename, "r+", encoding="utf-8") as f:
        value = f.readlines()
        print(value)
    with open(filename, "r+", encoding="utf-8") as f:
        f.writelines(["金1\n","音1\n","符1\n"])




read_all_lines("info.txt")

# 3、封装操作追加内容写入文件的函数
#追加在最后
def add_write(filename,content):
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(content)
# add_write("info.txt","aaaaaaaaa")

# writelines的运用
def add_writelines(filename,content):
    with open(filename, "a+", encoding="utf-8") as f:
        f.writelines(content)
# add_writelines("info.txt",["AA\n","BB\n","CC\n"])