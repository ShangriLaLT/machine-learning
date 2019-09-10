# 默认情况下 参数名和参数值，是根据参数定义顺序匹配的。
"""
参数传递问题，和可变类型与不可变类型

不可变类型：string number tuple
          a = 5  a = 10   意思是先创建了5让a指向5， 在创建了10 让a 指向10   5这个int值 a 被丢弃
   参数传递：值传递
可变类型：list dict
          a = {
            "key":"value"   
          }
          a['key']='value1'
          a 没有变，a 里面的值变化了。
   参数传递：引用传递
"""


# 不可变参数
def changeInt(a):
    a = 10


b = 2
changeInt(b)
print(b)


# 可变参数
def changeMe(a):
    a.append([1, 2, 3])


b = [1, 2, 3]
changeMe(b)
print(b)

"""
函数参数定义和调用
参数类型：
    必须参数
    关键字参数
    默认参数
    不定长参数
"""


# 1. 必须参数 (参数个数一致，顺序一致)
def test(a, body):
    print(a)
    print(body)


a = (1,)
b = {"body": "test"}
test(*a, **b)  # 必须传递两个参数要不然函数会报错

# 2.关键字参数
test(a=1, body=2)


# 3. 默认参数
# 可写函数说明
def test2(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


test2(name='litao', age=32)
test2(name='litaotao')


# 4. 不定长参数 可变参数必须在最后 （不定长参数的函数在调用的时候前面必须参数传递 不能 a = 1 这样关键字传递）

def test3(a, b, c=0, *d):
    print(a)
    print(b)
    print(c)
    print(d)


test3(1, 2, 3, 4, 5)  # 正确

# test3(a=1, b=2, c=3, d=(4, 5, 6))  # 错误

d = (4, 5, 6)
# test3(a=1, b=2, c=3, *d)  # 错误

test3(1, 2, 3, *d)  # 正确
test3(1, 2, 3, d)  # 正确  *d  d 的区别 d 是一个整体 *d 平铺d里面的值
test3(1, *d)  # 正确 先按照顺序赋值，剩余放在可变参数


def test4(a, b, c=0, **d):
    print(a)
    print(b)
    print(c)
    print(d)


test4(1, 2, 3, d=4, e=5)  # 正确  可变参数为 ** 的 后面可变参数部分必须以 d=4 3=5 参数形式调用。 而且不能用 a=5

test4(1, 2, c=3, d=4, e=5)  # 正确

# test4(1, b=2, 3, d=4, e=5)  # 错误

d = {'d': 4, 'e': 5}
# test4(1, 2, 3, d)  # 错误
test4(1, 2, 3, d=d)  # 正确
test4(1, 2, 3, **d)  # 正确

# d = {'a': 1, 'd': 4, 'e': 5}
# test4(1, 2, 3, d=d)  # 错误 因为 d 里面有参数 a


d = {'c': 3, 'd': 4, 'e': 5}
test4(1, 2, **d)  # 正确  先关键字匹配参数，多余的放在最后一个可变参数里面

"""
匿名函数
"""
