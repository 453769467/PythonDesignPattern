# -*- coding: UTF-8 -*-
"""
外观模式（Facade）
模式说明：
    为子系统中的一组接口提供一个一致的界面，定义一个高层接口，这个接口使得这一子系统更加容易使用。

意图：
    为子系统中的一组接口提供一个一致的界面，Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用

适用性：

    1. 设计初期阶段，应该有意识的将不同层分离，层与层之间建立外观模式。
    2. 开发阶段，子系统越来越复杂，增加外观模式提供一个简单的调用接口.
    3. 维护一个大型遗留系统的时候，可能这个系统已经非常难以维护和扩展，但又包含非常重要的功能，为其开发一个外观类，以便新系统与其交互.

优点：
    1. 实现了子系统与客户端之间的松耦合关系.
    2. 客户端屏蔽了子系统组件，减少了客户端所需处理的对象数目，并使得子系统使用起来更加容易.
缺点：
    ---

"""


def print_info(info):
    print(info)


class Stock():
    name = "股票"

    def buy(self):
        print_info("买 " + self.name)

    def sell(self):
        print_info("卖 " + self.name)


class ETF():
    name = "指数型基金"

    def buy(self):
        print_info("买 " + self.name)

    def sell(self):
        print_info("卖 " + self.name)


class Future():
    name = "期货"

    def buy(self):
        print_info("买 " + self.name)

    def sell(self):
        print_info("卖 " + self.name)


class NationDebt():
    name = "国债"

    def buy(self):
        print_info("买 " + self.name)

    def sell(self):
        print_info("卖 " + self.name)


class Option():
    name = "权证"

    def buy(self):
        print_info("买 " + self.name)

    def sell(self):
        print_info("卖 " + self.name)


class Fund():
    """
    基金
    """
    def __init__(self):
        self.stock = Stock()
        self.etf = ETF()
        self.future = Future()
        self.debt = NationDebt()
        self.option = Option()

    def buy_fund(self):
        self.stock.buy()
        self.etf.buy()
        self.future.buy()
        self.debt.buy()
        self.option.buy()

    def sell_fund(self):
        self.stock.sell()
        self.etf.sell()
        self.future.sell()
        self.debt.sell()
        self.option.sell()


def client_ui():
    fund = Fund()
    fund.buy_fund()
    fund.sell_fund()
    return


if __name__ == "__main__":
    client_ui()
    