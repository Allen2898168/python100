"""
    练习题15：判断是不是数字

    如何判断一个字符串是不是纯数字组成

"""

a = "1234"

if type(a) == int:
    print("a的类型是数字组成")
else:
    print("不是")

# try判断是否抛异常,兼容数字字符串
try:
    int(a)
    print(True)
except:
    print(False)
