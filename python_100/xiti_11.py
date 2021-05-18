"""
    练习题11：查找字符串首次出现的位置
    输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
    从 0 开始计数

    A = "hello"
    B = "hi how are you hello world, hello guoyupeng !"

"""

A = "hello"
B = "hi how are you hello world, hello guoyupeng !"

try:
    if B.index(A):
        print(B.index(A))
except:
    print(-1)



print(B.find(A))