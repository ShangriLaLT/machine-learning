"""
通过yield实现协程 next send.... close
"""


def grep(pattern):
    print("Looking for {}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print('{} : grep success '.format(line))


g = grep("python")
next(g)
print(11111)

print(g.send("test"))
print(11111)

print(g.send("python test"))
print(11111)

g.close()

"""
使用装饰器来实现协程
"""


def coroutine(func):
    def primer(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return primer


@coroutine
def grep(pattern):
    print("Looking for {}".format(pattern))
    try:
        while True:
            line = yield
            if line is None:
                break
            if pattern in line:
                print('{} : grep success '.format(line))
        return "over"
    except GeneratorExit:
        print("Goodbye!")
    except Exception as e:
        print(e)
        return "execpt over"


print("*" * 20)
g = grep("python")

g.send("python")
g.send("python")

# try:
#    g.throw(RuntimeError, "You're hosed")  # 也可以通过异常打断协程，并且获取返回值
# except StopIteration as e:
#     print(e.value)

"""
  g.close 关闭协程
"""
g.close()

try:
    g.send(None)  # 通过特殊参数结束协程
except StopIteration as e:
    print(e.value)  # 通过异常捕获获取协程返回值

print("*" * 20)
# g.close()

