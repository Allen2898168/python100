"""
    练习题18：字符串去掉左边指定空格或字符

    将字符串a = "  welcome to my world ！"左边的空格去掉

"""

a = "  welcome to my world ！"
print(a.lstrip())

# 只去除左边的！
a = "!welcome to my world ！"
print(a.lstrip("!"))
