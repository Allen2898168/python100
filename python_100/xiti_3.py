"""
    练习题3：字符串切割
    1.已知一个字符串为"hello_world_guoyupeng",
    如何得到一个队列 ["hello", "world", "guoyupeng"]

    2.让用户输入任意的用户名与密码，然后将他输入的用户名与 密码打印出来，
    如用户输入 abc/123 ，则打印
    您输入的用户名是: abc
    密码是:123
"""

a = "hello_world_guoyupeng"
print(a.split("_",1))



login = input("请输入账户密码，并以/分割")
b = login.split("/")
print(b[0])
print(b[1])
