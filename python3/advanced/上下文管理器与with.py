"""
上下文管理器通过with， 解决 try/finally模式
"""
import time
from contextlib import contextmanager

"""
 通过   contextmanager 装饰器  利用  try/finally  完成上下文管理器功能
"""


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('%s: %0.3f' % (label, end - start))


# Usage
with timethis('counting'):
    n = 1000000
    while n > 0:
        n -= 1

"""
一个普通的上下文管理器 需要有 __enter__  __exit__ 这两个方法
"""

import tempfile
import shutil


class tempdir(object):
    def __enter__(self):
        self.dirname = tempfile.mkdtemp()  # 生成临时文件夹
        return self.dirname

    def __exit__(self, exc, val, tb):
        shutil.rmtree(self.dirname)  # 删除文件夹


# Usage
with tempdir() as dirname:  # 执行了 __enter__
    # 执行业务逻辑
    pass
    # 执行 __exit__

"""
  上面的上下文管理器可以通过 contextmanager 装饰器  利用  try/finally  完成
"""

from contextlib import contextmanager


@contextmanager
def tempdir():
    dirname = tempfile.mkdtemp()
    try:
        yield dirname
    finally:
        shutil.rmtree(dirname)


# Usage
with tempdir() as dirname:  # 执行了 __enter__
    # 执行业务逻辑
    pass
    # 执行 __exit__

# 跟上个例子相同的代码。
