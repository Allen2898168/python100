# coding:utf-8
"""
    python笔记1
    假设你有无限数量的邮票,面值分别为6角，7角，8角,请问你最大的不可支付邮资是多少元？
"""
a = 6
b = 7
c = 8
t = 50
s = []

for i in range(t + 1):
    s1 = a * i
    s.append(s1)
    for j in range(t + 1):
        s2 = a * i + b * j
        s.append(s2)
        for k in range(t + 1):
            s3 = a * i + b * j + c * k
            s.append(s3)
s.sort()  # sort函数只是对list序列排序，从小到大排序，并没有返回值
news = []
for i in s:
    if i not in news:
        news.append(i)
print('组合生成的最大数%s' % news[-1])

r = []
for i in range(6 * t):
    if i in news:
        pass
    else:
        r.append(i)
print('组合不能生成的数字%s' % r)
print('不能生成的最大数字%s' % r[-1])
