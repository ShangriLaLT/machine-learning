"""
循环调用 else 当循环完成时进入，如果中途break就不会进入else逻辑
"""
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
else:
    print("test")

# for else

for i in range(10):
    if i % 2 == 0:
        continue
    if i == 7:
        break
    print(i)

else:
    print("end")

# for else 如果有break则不会进入 else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
