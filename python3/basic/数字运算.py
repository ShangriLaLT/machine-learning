# 数字之间转换
a = 1.0
b = int(a)
c = float(b)
d = complex(c)
# 相当于 a+bj b=0
e = complex(2, 3)
print(e)

# 数字运算
print(1 / 3)
print(1 // 3)
print(1.0 // 3)
print(2 * 3)
print(2 ** 3)
# 取余数
print(17 % 3)
print(17 / 3)
print(12.5e-2)
# 交互模式中最后一次运算结果赋值给了 _ (下划线)

# 数学函数
import math

# 绝对值
print(abs(-10))
print(math.fabs(-10))
# 向上进位
print(math.ceil(4.1))
# 向下进位
print(math.floor(4.9))
# log 对数 默认以e为底
print(math.log(math.e))
print(math.log(100, 10))
print(math.log10(100))
# max 返回给定参数的最大值，参数可以为序列。
# min
print(max((1, 2, 3, 4, 5)))
# 列表比较根据列表大小
print(min((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)))
# modf 返回整数和小数部分
print(math.modf(100.12))
# power 指数运算
print(math.pow(2, 3))
# sqrt 平方根运算
print(math.sqrt(4))
# round 四舍五入 第二位代表小数点后精确的位数
print(round(10.5647, 3))

# 随机数函数
import random

print("随机数函数")
# 在列表中随机一个
print(random.choice(range(10)))
# 1到10 跨度为2的数值里面随机一个
print(random.randrange(1, 10, 2))

# shuffle 将一个数组随机排序
r_a = [1, 2, 3, 4]
random.shuffle(r_a)
print(r_a)

# uniform(x, y) 1-10 里面随机生成一个实数
print(random.uniform(1, 10))

# 数字常量 π e
print(math.e)
print(math.pi)

# 三角函数 用的时候再查
print("三角函数")
print(math.acos(0.1))
