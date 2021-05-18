"""
    练习题12： 查找字符串最后一次出现的位置
    输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A,则输出-1
    从 0 开始计数
    A = "hello"
    B = "hi how are you hello world, hello guoyupeng !"


"""

A = "hello"
B = "hi how are you hello world, hello guoyupeng !"

# 从右边开始找
print(B.rfind(A))