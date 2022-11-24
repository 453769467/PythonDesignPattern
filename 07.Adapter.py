# -*- coding: UTF-8 -*-
"""
适配器模式（Adapter）
模式说明：
    ----

意图：
    将一个类的接口转换成客户希望的另外一个接口, Adapter 模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作

适用性：
    1. 你想使用一个已经存在的类，而它的接口不符合你的需求。
    2. 你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作。
    3. （仅适用于对象Adapter ）你想使用一些已经存在的子类，但是不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。

优点：
    ---
缺点：
    ---

Player：(父类or基类）
国内
Forwards（Player的子类or派生类）：作用为国内球员的动作方法
Center（Player的子类or派生类）：作用为国内球员的动作方法
Guards（Player的子类or派生类）：作用为国内球员的动作方法
国外：
ForeignCenter（Player的子类or派生类）：作用为国外球员的动作方法（动作虽然一样但是动作方法的名字和国内动作方法的名字不一样）
Translator（Player的子类or派生类）：作用为适配器，国内球员的动作方法的名字一样（但是方法内调用了国外球员对象的动作方法）
"""


def print_info(info):
    print(info)


class Player():
    """
    球员类
    """
    name = ""

    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defense(self):
        pass


class Forwards(Player):
    """
    前锋
    """
    def __init__(self, name):
        Player.__init__(self, name)

    def attack(self):
        print_info("前锋%s 进攻" % self.name)

    def defense(self):
        print_info("前锋%s 防守" % self.name)


class Center(Player):
    """
    中锋（目标类）
    """
    def __init__(self, name):
        Player.__init__(self, name)

    def attack(self):
        print_info("中锋%s 进攻" % self.name)

    def defense(self):
        print_info("中锋%s 防守" % self.name)


class Guards(Player):
    """
    后卫
    """
    def __init__(self, name):
        Player.__init__(self, name)

    def attack(self):
        print_info("后卫%s 进攻" % self.name)

    def defense(self):
        print_info("后卫%s 防守" % self.name)


class ForeignCenter(Player):
    """
    外籍中锋（待适配类）
    """
    name = ""

    def __init__(self, name):
        Player.__init__(self, name)

    def foreign_attack(self):
        print_info("外籍中锋%s 进攻" % self.name)

    def foreign_defense(self):
        print_info("外籍中锋%s 防守" % self.name)


class Translator(Player):
    """
    翻译（适配类）
    """
    foreign_center = None

    def __init__(self, name):
        self.foreign_center = ForeignCenter(name)

    def attack(self):
        self.foreign_center.foreign_attack()

    def defense(self):
        self.foreign_center.foreign_attack()


def client_ui():
    b = Forwards("巴蒂尔")
    ym = Guards("姚明")
    m = Translator("麦克格雷迪")

    b.attack()
    m.defense()
    ym.attack()
    b.defense()
    return


if __name__ == "__main__":
    client_ui()
    