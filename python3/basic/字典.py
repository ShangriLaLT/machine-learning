"""
字典是一个可变容器模型,且可以存储任意对象。
字典的键必须是不可变的比如，字符串，数字，元组。
键值可以是任意数据类型。
"""
dict1 = {"key1": "value1", "key2": "value2"}
# 访问
print(dict1["key1"])
print(dict1.get("key1", ""))

# 修改

dict1['key1'] = "value3"

print(dict1)

del dict1["key2"]

# 内置函数

# len  str  type

# 赋值字典
dict2 = dict1.copy()
# 清空字典
dict1.clear()

tuple1 = ("key1", "key2", "key3")

# 判断一个key是否在字典中

if "key1" in dict2:
    pass

# 遍历
for i, j in dict2.items():
    print("i:%s   j:%s" % (i, j))

# 遍历key
for key in dict2.keys():
    pass

# 遍历value
for value in dict2.values():
    pass

# 添加键值对
dict2.setdefault("key2", "value2")
dict2["key3"] = "value3"

# 更新 用dict1里面的键值对去更新dict2里面的值
dict2.update(dict1)

# 删除
dict2.pop("key3")

# 随机删除
dict2.popitem()

# 通过元组生成字典并且设置默认值

set3 = (1, 2, 3, 4)
dict3 = dict.fromkeys(set3, 10)
print(dict3)
