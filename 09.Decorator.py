# -*- coding: UTF-8 -*-
"""
装饰模式（Decorator）
模式说明：
    ---

意图：
    动态地给一个对象添加一些额外的职责。就增加功能来说，Decorator 模式相比生成子类更为灵活。

适用性：
    在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。
    处理那些可以撤消的职责。
    当不能采用生成子类的方法进行扩充时

优点：
    ---
缺点：
    ---

"""


class Foo(object):

    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class FooDecorator(object):

    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


if __name__ == "__main__":
    u = Foo()
    v = FooDecorator(u)
    v.f1()
    v.f2()
    