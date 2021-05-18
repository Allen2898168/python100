"""
    练习题4：拼接字符串
    有个列表 ["hello", "world", "guo"]

    如何把把列表里面的字符串联起来，

    得到字符串 "hello_world_guo"

"""

a = "hello,world,guo"
print(type(a))
a = a.split(",")
print(a)
print("_".join(a))