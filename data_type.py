"""
  python三大数据类型
  数值类型： 整数型、浮点数、布尔、复数
  序列类型： 列表、元组、字符串、二进制序列
  散列类型： 集合、 字典

"""

""" -------------------*数值类型*--------------------"""
# 整数型
a = 1
print(type(a))

# 浮点数
b = 1.1
print(type(b))

# 布尔类型
c = 1 == 2
print(type(c))

# 复数
complex1 = 22 + 12j
print('complex1 的类型为：', type(complex1))
print('复数 complex1 中的实部为：', complex1.real)
print('复数 complex1 中的虚部为：', complex1.imag)

""" -------------------*序列类型*--------------------"""
# 列表
d = []
print(type(d))

# 新增
d.append("guo")
print(d)

# 插入
d.insert(1, "hello")
print(d)

# append函数直接将object整体当作一个元素追加到列表中，而extend函数则是将可迭代对象中的元素逐个追加到列表中
d.extend(["yu", "peng"])
d.append(["yu", "peng"])
print(d)

e = [1, 2, 3, 4, 5, 6, '郭', '宇', '鹏']

# 从最后一个元素删除
e.pop()
print(e)

# 删除指定元素
e.remove(6)
print(e)

# 清空列表所有元素
e.clear()
print(e)

# 内置函数,删除指定元素
e = [1, 1, 2, 2, 3, 2, '郭', '宇', '鹏']
del e[2]
print(e)

# 修改
e[2] = 2
print(e)

# 查找指定元素的第一个下标
print(e.index(2))

# 统计指定元素个数
print(e.count(2))

# 字典 浅拷贝
f = {1: [1, 2, 3]}
j = f.copy()
print(j, f)
f[1].append(5)
print(j, f)

# 字典 深拷贝
import copy
g = copy.deepcopy(f)
print(g, f)
f[1].append(9)
print(g, f)




