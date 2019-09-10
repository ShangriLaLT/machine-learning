# python 一切皆对象。
# python 中所有的类都是有type() 方法创建。
# type 是类的类，属于元类。也就是说一个对象 class a();   a.__class__.__class__.class__ 最终类型肯定是type

# 通过type创建一个类


#  普通方法：要带有参数self,因为类中方法默认带self参数
def speak(self):
    print("这是给类添加的普通方法")


#  类方法
@classmethod
def c_run(cls):
    print("这是给类添加的类方法")


# 静态方法
@staticmethod
def s_eat():
    print("这是给类添加的静态方法")


class Person(object):
    def go(self):
        print("persion func go")


# 创建类，给类添加静态方法，类方法，普通方法。跟添加类属性差不多.
Boy = type("Boy", (Person,), {"speak": speak, "c_run": c_run, "s_eat": s_eat, "sex": "female"})
boy = Boy()
print(type(boy))
print(type(Boy))

boy.speak()
boy.s_eat()  # 调用类中的静态方法
boy.c_run()  # 调用类中类方法
print("boy.sex:", boy.sex)

# 继承类的方法
boy.go()
