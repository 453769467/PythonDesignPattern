# -*- coding: UTF-8 -*-
"""
访问者模式（Visitor）
模式说明：
    ---

意图：
    定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。TemplateMethod 使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

适用性：
    1. 一次性实现一个算法的不变的部分，并将可变的行为留给子类来实现。
    2. 各子类中公共的行为应被提取出来并集中到一个公共父类中以避免代码重复。首先识别现有代码中的不同之处，并且将不同之处分离为新的操作。
       最后，用一个调用这些新的操作的模板方法来替换这些不同的代码。
    3. 控制子类扩展。模板方法只在特定点调用“hook ”操作（参见效果一节），这样就只允许在这些点进行扩展

优点：
    ---
缺点：
    ---

"""


class Node(object):
    pass


class NodeA(Node):
    pass


class NodeB(Node):
    pass


class NodeC(Node):
    pass


class Visitor(object):
    def visit(self, node, *args, **kwargs):
        method = None
        for cls in node.__class__.__mro__:
            method_name = 'visit_' + cls.__name__
            method = getattr(self, method_name, None)
            if method:
                break

        if not method:
            method = self.generic_visit

        return method(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_b(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


if __name__ == "__main__":
    a = NodeA()
    b = NodeB()
    c = NodeC()

    visitor = Visitor()
    visitor.visit(a)
    visitor.visit(b)
    visitor.visit(c)

    visitor.visit_b(c)
    