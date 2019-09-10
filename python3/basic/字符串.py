a = 'Hello World!'
# 字符串截取
print("字符串截取[:1]", a[:1])
print("字符串截取[1]", a[1])
print("字符串截取[1:]", a[1:])
print("字符串截取[-2:]", a[-2:])
print("字符串截取[1:5]", a[1:5])

# 字符串更新
print("已更新字符串 : ", a[:6] + 'Runoob!')

# 转义字符
print("退格\\b:  !\b$")
print("空\\000:  !\000$")
print("换行\\n:  !\n$")
print("纵向制表符\\v:  !\v$")
print("横向制表符\\t:  !\t$")
print("回车\\r:  !\r$")
print("换页\\f:  !\f$")

# 字符串运算

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

# 字符串格式化

print("你好:%s,我今年%d岁了！" % ("李涛", 32))
print("格式化字符 %c" % 'a')
print("无符号整形  %d %u %x %o" % (10, 10, 10, 10))
print("格式化十六进制  %x %X" % (10, 10))
print("格式化浮点型  %f %e %E" % (1.0000001, 1.02e-2, 1.0000001))

# 三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

# 字符串内建函数
print("字符串首字母大写", str.capitalize("hello"))
print("字符串居中", "hello".center(10, "*"))
print("字符串中字符串出现的次数", "hello".count("l"))
ec = "中文".encode(encoding="utf-8")
print("字符串编码", ec)
print("字符串解码", ec.decode(encoding="utf-8"))
print("字符串结束字符", "hello world".endswith("world"))
print("字符串开始字符", "hello world".endswith("hello", 0, 5))
print("字符串tab转空格", "hello\tworld".expandtabs(tabsize=20))
print("字符串查找 rfind 从右边开始", "hello world".find("world", 5, len("hello world")))
try:
    print("字符串查找 rindex 从右边开始", "hello world".index("world", 7, len("hello world")))
except ValueError as e:
    print(e)
# find index 区别在于index如果找不到不是返回-1而是报错

print("字符串全是字母或者数字", "hello world 007".isalnum(), )
print("字符串全是字母或者数字", "hello007".isalnum(), )
print("字符串全是字母", "hello007".isalpha(), )
print("字符串全是字母", "hello".isalpha(), )
print("字符串全是数字", "007".isdigit(), "三".isnumeric())
# isdigit isnumeric 包括汉语数字
print("字符串是否只包含十进制数", "7".isdecimal(), )
print("字符串是否大小写", "Test".lower().islower(), )
print("字符串是否大小写", "Test".upper().isupper(), )

print("字符串是否只包含空格", "hello world".isspace(), )
print("字符串是否包含空格", "   ".isspace(), )
print("字符串是否标题化的", "Hello World".istitle(), )
print("字符串是否标题化的", "Hello world".istitle(), )
print("列表转化成字符串", ",&".join(["1", "2", "3", "4", "5"]))
print("字符串长度", len("Hello World!"))
print("字符串左对齐,补充到指定大小,如果本身就大于指定大小返回本身 ljust 左对齐  rjust 右对齐 zfill() 右对齐前面填充0 ", "Hello World".ljust(50, "*"))
print("截掉字符串左边的指定字符可以是空格 rstrip 右边", "*****Hello World".lstrip("*"))
# 字符串对应表替换
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print(str.translate(trantab))
# 返回字符串最大最小字符

print("字符串替换 可以指定替换次数", "Hello World".replace(" ", "*"))
print("字符串切割 可以指定切割次数", "Hello World".split(" "))
print("字符串去掉两边空格 strip", "  Hello World  ".strip())

print("标题化显示字符串 title()")
print("大写转换成小写,小写转换成大写 swapcase()")


