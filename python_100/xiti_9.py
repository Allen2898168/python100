"""
    练习题9: 统计每个字符出现次数

"""
import json
from collections import Counter

a = "Hello, welcome to my world."

b = Counter(a)



s = []

for i, j in dict(b).items():
    print(i, j)
    if j == 1:
        s.append(i)
print(s)

# 列表推导式
s = [i for i, j in dict(b).items() if j == 1]
print(s)