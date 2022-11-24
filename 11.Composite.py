# -*- coding: UTF-8 -*-
"""
组合模式（Composite）
模式说明：
    ---

意图：
    将对象组合成树形结构以表示“部分-整体”的层次结构, Composite 使得用户对单个对象和组合对象的使用具有一致性

适用性：
    1. 想表示对象的部分-整体层次结构
    2. 希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象

优点：
    ---
缺点：
    ---

"""


class Component:
    def __init__(self, str_name):
        self.m_str_name = str_name

    def add(self, com):
        pass

    def display(self, num_depth):
        pass


class Leaf(Component):
    def add(self, com):
        print("leaf can't add")

    def display(self, num_depth):
        str_temp = "-" * num_depth
        str_temp = str_temp + self.m_str_name
        print(str_temp)


class Composite(Component):
    def __init__(self, str_name):
        self.m_str_name = str_name
        self.c = []

    def add(self, com):
        self.c.append(com)

    def display(self, num_depth):
        str_temp = "-" * num_depth
        str_temp = str_temp + self.m_str_name
        print(str_temp)
        for com in self.c:
            com.display(num_depth + 2)


if __name__ == "__main__":
    p = Composite("Wong")
    p.add(Leaf("Lee"))
    p.add(Leaf("Zhao"))

    p1 = Composite("Wu")
    p1.add(Leaf("San"))
    p.add(p1)
    p.display(1)
    