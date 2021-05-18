"""
    练习题7：字符串下标
    找出单词 “welcome” 在 字符串“Hello, welcome to my world.” 中出现的位置，找不到返回-1
    从下标0开始索引

"""

a = 'Hello, welcome to my world.'

if "welcome" in a:
    print(a.index("welcome"))
else:
    print(-1)

# 三元表达式
print(a.index('welcome') if "welcome" else -1)
