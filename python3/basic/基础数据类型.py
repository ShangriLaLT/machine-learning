# 基本数据类型  变量没有类型 变量所指的内存空间数据有类型。
# int
a = 1
print(isinstance(a, int))  # isinstance 会考虑父类继承关系
print(type(a))  # type 不考虑继承关系

# float
b = 1.0
print(type(b))

# string
c = "String"
print(type(c))

# boolean
d = True
print(type(d))

# 复数
e = 4 + 3j
print(type(e))

# list
f = [1, 2]
print(type(f))

# tuple
g = (1, "2")
print(type(g))

# dict
h = {"a": 1}
print(type(h))
