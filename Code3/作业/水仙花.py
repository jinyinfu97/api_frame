# 水仙花数
# for num in range(100,1000):
#     s = 0
#     a = list(str(num))
#     for i in a:
#         s = s + int(i)**3
#     # print(s)
#     if s == num:
#         print("{0}是水仙花数".format(num))

# 如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备数。
# 例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加， 1+2+3=6。
# 第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
# 那么问题来了，求1000以内的完全数有哪些？

# for i in range(1,1001):
#     sum = 0
#     for n in range(1,i):
#         if i%n == 0:
#             sum = sum+n
#     if sum == i:
#         print(f"{i}是完全数")

# 有写公司会要求能写一小段程序出来，
# 如题： 写一个小程序：控制台输入邮箱地址（格式为username@companyname.com），
# 程序识别用户名和公司名后，将用户名和公司名输出到控制台。
# 要求： 1. 校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提示"incorrect email format"。注意必须以.com结尾
# 2. 可以循环“输入--输出判断结果”这整个过程
# 3. 按字母Q（不区分大小写）退出循环，结束程序


def test():
    email = input("请输入邮箱地址：")
    if email.upper() != "Q":
        if "@" in email and ".com" in email:

            num = 0
            for i in range(0, len(email)):
                if email[i] == "@" and email[0] != '@':
                    print(f"用户名为：{email[0:i]}")

                    num = num + i
                elif email[i] == "@" and email[0] == "@":
                    print("用户名不能为空！")
                    test()
                    # print(i)

            for n in range(0, len(email)):
                if email[n:n + 4] == ".com" and email[n - 1] != '@':

                    # print(n)
                    print(f"公司名为：{email[num + 1:n]}")
                    print(f"{email}是个邮箱")
                elif email[n:n + 4] == ".com" and email[n - 1] == '@':
                    print("公司名不能为空！")
        else:
            print("incorrect email format")
        test()
    elif email.upper() == "Q":
        exit()

test()
