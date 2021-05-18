"""
    练习题14：判断一个姓名是否姓王
    输入一个姓名，判断是否姓王

"""


name = input("请输入你的姓名：")
if name.startswith("王"):
    print("姓王")
else:
    print("不姓王")

if name.endswith("三"):
    print("名字以三结尾")
else:
    print("名字非以三结尾")

