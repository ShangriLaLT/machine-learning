list = [1, 2, 3, "hello", "world"]
# 列表截取
print("列表截取", list[:2])
# 列表更新
list[2] = 4
# 列表删除
del list[1]
print(list)
# 列表叠加
list = list + ["!"]
print(list)

# 列表大小
print(len(list))

# 判断是否存在
print(2 in list)

# 列表函数
# len max min list (将元组转换成列表)
# 在列表结尾添加元素
list.append("nihao")
list.append("hello")
print(list)
# 统计元素出现的次数
print(list.count("hello"))
# 列表后面追加一个列表
list.extend([3, 6, 9])
print(list)
# 查找列表中某个元素第一次出现的位置。
print(list.index(3))

# 将一个对象插入到指定位置，可以是任意对象 后面元素统一后移
list.insert(7, {"key": 3})
print(list)

# 列表pop 默认最后一个可以指定索引,并返回删除的值
print(list.pop(7))
print(list)

# 删除第一次匹配的值
list.remove("hello")
print(list)

# 列表反向
list.reverse()
print(list)

# 列表拷贝
list2 = list.copy()

# 清空列表
list.clear()
print(list)
print(list2)

list = [{"key": 3}, {"key": 4}, {"key": 2}, {"key": 1}]

# sort sorted 区别
"""
sort 是应用在 list 上的方法，属于列表的成员方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
sort使用方法为ls.sort()，而sorted使用方法为sorted(ls)
"""


def sortFun(item):
    return item["key"]


list.sort(key=sortFun)
print(list)

list.sort(key=sortFun, reverse=True)
print(list)

# sorted 返回一个新的值。
# lambda 函数就是快速创建匿名函数并不会提高效率
print(sorted(list, key=lambda x: x["key"]))
print(sorted(list, key=sortFun))
print(sorted(list, key=sortFun, reverse=True))

# filter map 在 python3中返回一个迭代器需要遍历获取值。
# reduce 在python3中 放在了functools里面

print(filter(lambda x: x["key"] == 4, list))
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
for i in filter(lambda x: x % 3 == 0, foo):
    print(i)
print(map(lambda x: x * 2 + 10, foo))
import functools

print(functools.reduce(lambda x, y: x + y, foo))
# 元组

# 当元组只有一个元素的时候后面需要用逗号
# int
print(type((5)))
# tuple
print(type((5,)))

"""
   访问元组
"""

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组
del tup3

"""
  元组内置函数
  
  len  max  min  tuple
"""