import turtle
"""
    循环绘制五角星
    turtle 教程
    https://docs.python.org/zh-cn/3.7/library/turtle.html
"""

import matplotlib

# Force matplotlib to not use any Xwindows backend.

matplotlib.use('Agg')

tt = turtle.Turtle()


def paint_start(side_length):
    """
    绘制五角星
    :param side_length: 五角星边长
    :return:
    """
    index = 0
    # 在python中 for循环是for in语法
    while index < 5:
        # 前进一个定常,也就是画一条边
        tt.forward(side_length)
        # 转角,顺时针旋转
        tt.right(144)
        # 画一条边
        tt.forward(side_length)
        index += 1


def loop_paint(time_num, side_length):
    i = 0
    while i < time_num:
        paint_start(side_length)
        # 抬起画笔,后面的不会画出来，方便调整位置
        tt.penup()