# -*- coding: UTF-8 -*-
"""
抽象工厂模式（Abstract Factory）
模式说明：
    抽象工厂模式是对象的创建模式，它是工厂方法模式的进一步推广

意图：
    抽象工厂的功能是为一系列相关对象或相互依赖的对象创建一个接口

适用性：
    这个接口内的方法不是任意堆砌的，而是一系列相关或相互依赖的方法。比如主板和CPU，都是为了组装一台电脑的相关对象。不同的装机方案，代表一种具体的电脑系列。
    1. 一个系统不应当依赖于产品类实例如何被创建、组合和表达的细节，这对于所有形态的工厂模式都是重要的
    2. 这个系统的产品有多于一个的产品族，而系统只消费其中某一族的产品
    3. 同属于同一个产品族的产品是在一起使用的，这一约束必须在系统的设计中体现出来
    4. 系统提供一个产品类的库，所有的产品以同样的接口出现，从而使客户端不依赖于实现
优点：
    分离接口和实现:
    客户端使用抽象工厂来创建需要的对象，而客户端根本就不知道具体的实现是谁，客户端只是面向产品的接口编程而已。
    也就是说，客户端从具体的产品实现中解耦。
    使切换产品族变得容易：
    因为一个具体的工厂实现代表的是一个产品族，比如上面例子的从Intel系列到AMD系列只需要切换一下具体工厂

缺点：
    不太容易扩展新的产品：
    如果需要给整个产品族添加一个新的产品，那么就需要修改抽象工厂，这样就会导致修改所有的工厂实现类

AbstractFactory（父类or基类 ）
    IntelFactory（AbstractFactory的子类or派生类）：作用为进行了创建自定品牌的零件
    AmdFactory（AbstractFactory的子类or派生类）：作用为进行了创建自定品牌的零件
AbstractCpu（父类or基类 ）
    IntelCpu（AbstractCpu的子类or派生类）：作用为记录cup的型号
    AmdCpu（AbstractCpu的子类or派生类）：作用为记录cup的型号
AbstractMainBoard（父类or基类 ）
    IntelMainBoard（AbstractMainBoard）：作用为记录主板的型号
    AmdMainBoard（AbstractMainBoard 的子类or派生类）：作用为记录主板的型号
ComputerEngineer（新式类）：作用为根据工厂对象（如IntelFactory()）让其组装自身型号的零件
"""

__author__ = "Burgess Zheng"
# !/usr/bin/env python
# -*- coding:utf-8 -*-


class AbstractFactory(object):
    """
    抽象工厂
    """
    computer_name = ''

    def create_cpu(self):
        pass

    def create_main_board(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer '

    def create_cpu(self):
        return IntelCpu('I7-6500')

    def create_main_board(self):
        return IntelMainBoard('Intel-6000')


class AmdFactory(AbstractFactory):
    computer_name = 'Amd 4 computer '

    def create_cpu(self):
        return AmdCpu('amd444')

    def create_main_board(self):
        return AmdMainBoard('AMD-4000')


class AbstractCpu(object):
    series_name = ''
    instructions = ''
    arch = ''


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AbstractMainBoard(object):
    series_name = ''


class IntelMainBoard(AbstractMainBoard):
    def __init__(self, series):
        self.series_name = series


class AmdMainBoard(AbstractMainBoard):
    def __init__(self, series):
        self.series_name = series


class ComputerEngineer(object):

    def make_computer(self, factory_obj):
        self.prepare_hardwares(factory_obj)

    def prepare_hardwares(self, factory_obj):
        self.cpu = factory_obj.create_cpu()
        self.main_board = factory_obj.create_main_board()

        info = '''
        ------- 
        computer [%s] info:
        cpu: %s
        main_board: %s
        -------- End --------
        ''' % (factory_obj.computer_name, self.cpu.series_name, self.main_board.series_name)
        print(info)


if __name__ == "__main__":
    engineer = ComputerEngineer()  # 装机工程师

    intel_factory = IntelFactory()  # intel工厂
    engineer.make_computer(intel_factory)

    amd_factory = AmdFactory()  # adm工厂
    engineer.make_computer(amd_factory)