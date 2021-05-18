"""
    练习题2：回本
    回文的定义： "回文"就是正读倒读都一样的。

    如奇数个： "98789" ，这个数字正读是"98789" 倒读也是"98789"。
    偶数个数字"3223"也是回文数。
    字母 "abcba" 也是回文。

    判断一个字符串是否是回文字符串，是打印True， 不是打印False
"""
# 1.切片  前闭后开 步长-1 反转字符串
a = 'abcba'
print(a == a[::-1])

# 2.reversed

b = reversed(a)  # reversed  object迭代器
c = "".join(b)
print(a == c)
print(a == "".join(reversed(a)))     # 可以一段代码实现 判断一个字符串是否是回文字符串


