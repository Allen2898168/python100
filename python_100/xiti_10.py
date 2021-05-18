"""
    练习题9: 判断字符a含b
    判断字符串a="Hello, welcome to my world." 是否包含单词b="world"
    包含返回True，不包含返回 False

"""
import json
from collections import Counter

a = "Hello, welcome to my world."

b = "world"


if b in a:
    print(True)
else:
    print(False)



print(b in a)


if a.find(b) is not -1:
    print(True)
else:
    print(False)


print(True if a.find(b) is not -1 else False)


