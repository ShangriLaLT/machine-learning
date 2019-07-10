# 注释#号后面需要空格

"""
python3默认编码是UTF-8,所有的字符串都是unicode,可以通过
#  -*- coding: cp-1252 -*-  来修改文件编码

1. 计算机 单片机 只知道 0 1
2. 怎么表示英文字母和标点符号？ 那就出现了 ASCII 用一个字节=8bit有256个标识符来表示。
3. 那么其它特殊语言怎么办？ 只能用2个字节=16bit或者4个字节来表示更多的信息。这就提出来了 unicode
4. UTF-8是可变字节1~6个字节兼容ASCII和UNICODE。
5. UTF-16 .....
"""
if __name__ == '__main__':
    print("你好")
    import keyword

    # 保留字
    print(keyword.kwlist)

    # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    print("litao", "ni", "zui", "bang", sep="&", end="#")
