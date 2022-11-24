# -*- coding: UTF-8 -*-
"""
享元模式（Flyweight）
模式说明：
    ---

意图：
    运用共享技术有效地支持大量细粒度的对象。

适用性：
    1. 当一个应用程序使用了大量的对象。
    2。 由于使用大量的对象，造成很大的存储开销
    3。 对象的大多数状态都可变为外部状态
    4。 如果删除对象的外部状态，那么可以用相对较少地共享对象取代很多组对象
    5。 应用程序不依赖于对象标识。由于Flyweight 对象可以被共享，对于概念上明显有别的对象，标识测试将返回真值。

优点：
    ---
缺点：
    ---

"""


class FlyWeightBase(object):
    _instances = dict()     # 被实例化的对象内存地址

    def __init__(self, *args, **kwargs):
        """
        继承的子类必须初始化
        :param args:
        :param kwargs:
        """
        raise NotImplementedError

    def __new__(cls, *args, **kwargs):
        print(cls._instances, type(cls))    # cls 就是要实例化的子类
        return cls._instances.setdefault(
            (cls, args, tuple(kwargs.items())),
            super(FlyWeightBase, cls).__new__(cls)
        )


class Spam(FlyWeightBase):
    """
    精子类
    """
    def test_data(self):
        pass

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test_data(self):
        print("精子准备好了", self.a, self.b)


class Egg(FlyWeightBase):
    """
    卵类
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def test_data(self):
        print("卵子准备好了", self.x, self.y)


if __name__ == "__main__":
    spam1 = Spam(1, "abc")
    spam2 = Spam(1, "abc")
    spam3 = Spam(3, "DEF")

    egg1 = Egg(1, "abc")
    print(id(spam1), id(spam2), id(spam3))
    