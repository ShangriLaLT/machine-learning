# 算数运算
a = 21
b = 10
c = 0

c = a + b
print("a + b 的值为：", c)

c = a - b
print("a - b 的值为：", c)

c = a * b
print("a * b 的值为：", c)

c = a / b
print("a / b 的值为：", c)

c = a % b
print("a % b 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("a ** b 的值为：", c)

a = 10
b = 5
c = a // b
print("a // b 的值为：", c)

# 比较运算符
# < > = >= <= == !=


# 赋值运算

print("赋值运算")

c = a + b
print("c = a + b 的值为：", c)

c += a
print("c += a 的值为：", c)

c *= a
print("c *= a 的值为：", c)

c /= a
print("c /= a 的值为：", c)

c = 2
c %= a
print("c %= a 的值为：", c)

c **= a
print("c **= a 的值为：", c)

c //= a
print("c //= a 的值为：", c)

# 位运算
print("位运算")

"""

a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100   //两个都为真

a|b = 0011 1101   //有一个为真

a^b = 0011 0001   //两个不同

~a  = 1100 0011   //取反
"""
a = 60
c = 0
c = a << 2  # 240 = 1111 0000
print("c = a << 2 的值为：", c)

c = a >> 2  # 15 = 0000 1111
print("c = a >> 2的值为：", c)

print("60 的二进制", bin(60))

# 成员运算
# in  not in

# 逻辑运算
# and  or  not

# 身份运算
# is  is not
