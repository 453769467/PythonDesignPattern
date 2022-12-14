# -*- coding: UTF-8 -*-
"""
单例模式（Singleton）
模式说明：
    ----

意图：
    保证一个类仅有一个实例，并提供一个访问它的全局访问点

适用性：
    当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时
    当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时

优点：
    ---
缺点：
    ---

"""


class Singleton(object):
    """
    单例模式（Singleton）
    实现__new__方法, 并在将一个类的实例绑定到类变量_instance上,
    如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
    如果cls._instance不为None,直接返回cls._instance
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)    # 让cls继承指定的父类 Singleton
            cls._instance = orig.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


class Nana(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    a = MyClass("Burgess")
    print(a.name)
    b = MyClass("Crystal")
    print(a.name)
    print(b.name)
    b.name = "xx"
    print(a.name)
    print(b.name)
    