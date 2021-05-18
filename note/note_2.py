"""
    python笔记2
    冒泡排序
"""

li = [12, 4, 5, 6, 7, 89, 3, 23, 2]
for i in range(len(li)):
    x = len(li) - i - 1
    for j in range(x):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)


# python里面排序不用这么麻烦，一个函数搞定：sort()
li = [12, 4, 5, 6, 4, 89, 3, 23, 2]

li.sort()
print(li)