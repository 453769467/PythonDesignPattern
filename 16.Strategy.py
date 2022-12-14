# -*- coding: UTF-8 -*-
"""
策略模式（Strategy）
模式说明：
    ---

意图：
    定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化.

适用性：
    1. 许多相关的类仅仅是行为有异, “策略”提供了一种用多个行为中的一个行为来配置一个类的方法。
    2. 需要使用一个算法的不同变体, 例如，你可能会定义一些反映不同的空间/时间权衡的算法。当这些变体实现为一个算法的类层次时,可以使用策略模式。
    3. 算法使用客户不应该知道的数据, 可使用策略模式以避免暴露复杂的、与算法相关的数据结构.
    4. 一个类定义了多种行为, 并且这些行为在这个类的操作中以多个条件语句的形式出现, 将相关的条件分支移入它们各自的Strategy类中以代替这些条件语句

优点：
    ---
缺点：
    ---

"""


class TravelStrategy(object):
    """
    出行策略
    """
    def travel_algorithm(self):
        pass


class AirplaneStrategy(TravelStrategy):
    """
    飞机出行
    """
    def travel_algorithm(self):
        print("坐飞机出行....")


class TrainStrategy(TravelStrategy):
    """
    高铁出行
    """
    def travel_algorithm(self):
        print("坐高铁出行....")


class CarStrategy(TravelStrategy):
    """
    自驾出行
    """
    def travel_algorithm(self):
        print("自驾出行....")


class BicycleStrategy(TravelStrategy):
    """
    骑车出行
    """
    def travel_algorithm(self):
        print("骑车出行....")


class TravelInterface(object):
    def __init__(self, travel_strategy):
        self.travel_strategy = travel_strategy

    def set_strategy(self, travel_strategy):
        self.travel_strategy = travel_strategy

    def travel(self):
        return self.travel_strategy.travel_algorithm()


if __name__ == "__main__":
    travel = TravelInterface(AirplaneStrategy())
    travel.travel()

    # 改开车
    travel.set_strategy(CarStrategy())
    travel.travel()
    