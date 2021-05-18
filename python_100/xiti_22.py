"""
    练习题22 ：字符串去重后保留顺序

    s = "ajldjlajfdljfddd"，去重保留原来的顺序，输出"ajldf"



"""

s = "ajldjlajfdljfddd"

b = "".join(set(s))

print("".join(sorted(b, key=lambda x: s.index(x))))



