"""
模块导入：
   import 放在顶部就是全局导入,放在函数里面就是局部导入,  第一次导入加载执行。
   from XX import 最好不要import * 变量会覆盖, 用from导入比如有多个模块依赖导入,编译器只会在第一次导入。
设置默认执行器：
   # !/usr/bin/python3
"""

import sys, getopt


def usage(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        """
          getopt 详解：
          入参：
            第一个是命令行参数
            第二个标识参数有 -h -i -o      -i 和 -o 后面有:(冒号)标识后面必须有值。
            第三个长参数--ifile --ofile 后面有=（等号）表示参数必须有值。
          返回值：
            第一个是一个元祖(（-i,test.py）,(-o,out.py))
            第二个参数是一个数组存放没有以 - 或者 -- 开始的值。
        """
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)


if __name__ == '__main__':
    usage(sys.argv[1:])
