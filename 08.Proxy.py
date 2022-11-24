# -*- coding: UTF-8 -*-
"""
代理模式（Proxy）
模式说明：
    在直接访问对象时带来的问题，比如说：要访问的对象在远程的机器上。在面向对象系统中，有些对象由于某些原因（比如对象创建开销很大，或者某些操作
    需要安全控制，或者需要进程外的访问），直接访问会给使用者或者系统结构带来很多麻烦，我们可以在访问此对象时加上一个对此对象的访问层

意图：
    为其他对象提供一种代理以控制对这个对象的访问

适用性：
    1. 想在访问一个类时做一些控制。

优点：
    1、职责清晰。 2、高扩展性。 3、智能化
缺点：
    1. 由于在客户端和真实主题之间增加了代理对象，因此有些类型的代理模式可能会造成请求的处理速度变慢
    2. 实现代理模式需要额外的工作，有些代理模式的实现非常复杂

SenderBase（父类or基类）
SendClass（SenderBase的子类or派生类）：作用为发送信息
AgentClass（SenderBase的子类or派生类）：作用为代理（发送信息给接受者）
ReceiveClass（新式类）：作用为实例化一个接受者
"""


class SenderBase:
    """
    父类or基类
    """
    def __init__(self):
        pass

    def send_something(self, something):
        pass


class SendClass(SenderBase):
    def __init__(self, receiver):
        self.receiver = receiver

    def send_something(self, something):
        print("SEND " + something + ' TO ' + self.receiver.name)


class AgentClass(SenderBase):
    def __init__(self, receiver):
        self.send_obj = SendClass(receiver)

    def send_something(self, something):
        self.send_obj.send_something(something)


class ReceiveClass:
    def __init__(self, someone):
        self.name = someone


if __name__ == "__main__":
    receiver = ReceiveClass("Burgess")
    agent = AgentClass(receiver)
    agent.send_something("agent_info")

    print(receiver.__class__)
    print(agent.__class__)
    