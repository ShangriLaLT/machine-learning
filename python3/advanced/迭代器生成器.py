"""
迭代器：需要有__iter__和__next__方法 for 可以遍历迭代器
"""

# 创建迭代器
a = [1, 2, 3, 4, 5]
iter_a = iter(a)
for i in iter_a:
    print(i)

# 到此 iter_a 已经迭代完成，不可逆转，如果继续 netx(iter_a) 就回抛错。
iter_b = iter(a)
while True:
    try:
        print(next(iter_b))
    except StopIteration:
        print("ok")
        break


# 创建一个迭代器


class MyIter(object):
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        if 10 < self.a:
            raise StopIteration
        return x


my = MyIter()
myIter = iter(my)

while True:
    try:
        print(next(myIter))
    except StopIteration:
        break


# 生成器 yield 配合 next 使用  yield 保存现场  next 拿到现场数据  yield 继续执行。


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        print("end")
        break
