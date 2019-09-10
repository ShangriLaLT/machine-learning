"""
集合一个无序不重复序列

"""
# a = set('abcd')
# b = set("cdef")
a = set(['a', 'b', 'c', 'd'])
b = set(['c', 'd', 'e', 'f'])

# 集合a中包含而集合b中不包含的元素

print(a - b)
print(type(a - b))

# 集合a或b中包含的所有元素 并集
print(a | b)

# 集合a和b中都包含了的元素 交集
print(a & b)

# 不同时包含于a和b的元素  去掉重复的
print(a ^ b)

# 集合推导式
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

# 集合的基本操作
iset = {1, 2, 3, 4}
iset.add(5)
print(iset)

iset.add((6, 7))
print(iset)

iset.update((5, 6, 7))

iset.update({5, 6, 7, 8})
print(iset)

iset.update([8, 9], [9, 10])
print(iset)

iset.remove((6, 7))
print(iset)

# discard 删除集合中的一个元素 和 remove 的区别是就算没有也不会抛错
iset.discard(11)

# pop 随机删除一个元素，交互模式中式删除第一个
iset.pop()
print(iset)

# 计算集合大小
len(iset)

# 清空结合
iset.clear()

# 拷贝
iset1 = iset.copy()

# x 中有 y 中没有的
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)

# 移除 x y 中有的
x.difference_update(y)
print(x)

# 返回集合的交集
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x.intersection_update(y)
print(x)

# 判断两个集合是否有交集
print(x.isdisjoint(y))

# 判断是否为子集
print(x.issubset(y))
print(x.issuperset(y))


# 返回两个集合不重复的元素。并集 减去 交集
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.symmetric_difference(y)

print(z)

x.symmetric_difference_update(y)
print(x)

# 返回两个集合的并集 重复元素只返回一次
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.union(y)

print(z)
