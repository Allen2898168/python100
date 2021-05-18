"""
    练习题20 ：去除字符串里面所有的空格


    将字符串a = "  welcome to my world !  "里面的所有空格都去掉



"""

a = "  welcome to my world !  "

print(a.replace(" ", ""))

# 也可以用split()切割后合并
print("".join(a.split(" ")))