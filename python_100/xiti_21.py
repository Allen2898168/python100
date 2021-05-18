"""
    练习题21 ：字符串去重后排序

    s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"


"""

s = "ajldjlajfdljfddd"
si = []

for i in s:
    if i not in si:
        si.append(i)
print(si)

print("".join(sorted(si)))

# 集合（set）  sorted() 是python里面的一个内建函数,用于排序
s = "ajldjlajfdljfddd"
print("".join(sorted(set(s))))
