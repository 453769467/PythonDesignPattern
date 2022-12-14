# -*- coding: UTF-8 -*-
"""
观察者模式（Observer）
模式说明：
    观察者（Observer）模式又名发布-订阅（Publish/Subscribe）模式, 当我们希望一个对象的状态发生变化，
    那么依赖与它的所有对象都能相应变化(获得通知),那么就可以用到Observer模式， 其中的这些依赖对象就是观察者的对象，
    那个要发生变化的对象就是所谓’观察者'

意图：
    定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时, 所有依赖于它的对象都得到通知并被自动更新。

适用性：
    1. 当一个抽象模型有两个方面, 其中一个方面依赖于另一方面。将这二者封装在独立的对象中以使它们可以各自独立地改变和复用。
    2. 当对一个对象的改变需要同时改变其它对象, 而不知道具体有多少对象有待改变。
    3. 当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之, 你不希望这些对象是紧密耦合的。

优点：
    ---
缺点：
    ---

"""


class ObserverBase(object):
    """
    放哨者
    """
    def __init__(self):
        self._observer_list = []    # 被通知对象

    def attach(self, observe_subject):
        """
        添加要观察的对象
        :param observe_subject:
        :return:
        """
        if observe_subject not in self._observer_list:
            self._observer_list.append(observe_subject)
            print("[%s]已经将[%s]加入观察队列..."%(self.name, observe_subject))

    def detach(self, observe_subject):
        """
        解除观察关系
        :param observe_subject:
        :return:
        """
        try:
            self._observer_list.remove(observe_subject)
            print("不再观察[%s]"%observe_subject)
        except ValueError:
            pass

    def notify(self):
        """
        通知所有被观察者
        :return:
        """
        for obj_server in self._observer_list:
            obj_server.update(self)


class Observer(ObserverBase):
    """
    观察者类
    """
    def __init__(self, name):
        super(Observer, self).__init__()
        self.name = name
        self._msg = ""

    @property
    def msg(self):
        """
        当前状况
        :return:
        """
        return self._msg

    @msg.setter
    def msg(self, content):
        self._msg = content
        self.notify()


class GCDViewer(object):
    """
    共军被观察者
    """
    def update(self, observer_subject):
        print("共军:收到[%s]消息[%s] " % (observer_subject.name, observer_subject.msg))


class GMDViewer(object):
    """
    国军被观察者
    """
    def update(self, observer_subject):
        print("国军:收到[%s]消息[%s] "%(observer_subject.name, observer_subject.msg))


if __name__ == "__main__":
    observer1 = Observer("共军放哨者")
    observer2 = Observer("国军放哨者")

    gongjun1 = GCDViewer()
    guojun1 = GMDViewer()

    observer1.attach(gongjun1)
    observer1.attach(guojun1)

    observer2.attach(guojun1)

    observer1.msg = "\033[32;1m敌人来了...\033[0m"
    observer2.msg = "\033[31;1m前方发现敌人,请紧急撤离,不要告诉共军\033[0m"
