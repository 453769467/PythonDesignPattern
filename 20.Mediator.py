# -*- coding: UTF-8 -*-
"""
调停者模式（Mediator）
模式说明：
    ---

意图：
    用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。

适用性：
    1. 一组对象以定义良好但是复杂的方式进行通信。产生的相互依赖关系结构混乱且难以理解。
    2. 一个对象引用其他很多对象并且直接与这些对象通信,导致难以复用该对象。
    3. 想定制一个分布在多个类中的行为，而又不想生成太多的子类。

优点：
    ---
缺点：
    ---

"""
import time


class TC:
    def __init__(self):
        self._tm = None
        self._b_problem = 0

    def setup(self):
        print("Setting up the Test")
        time.sleep(1)

    def execute(self):
        if not self._b_problem:
            print("Executing the test")
            time.sleep(1)
        else:
            print("Problem in setup. Test not executed.")

    def tear_down(self):
        if not self._b_problem:
            print("Tearing down")
            time.sleep(1)
            self._tm.publish_reporter()
        else:
            print("Test not executed. No tear down required.")

    def set_tm(self, tm):
        self._tm = tm

    def set_problem(self, value):
        self._b_problem = value


class Reporter:
    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Reporter Class is preparing to report the results")
        time.sleep(1)

    def report(self):
        print("Reporting the results of Test")
        time.sleep(1)

    def set_tm(self, tm):
        self._tm = tm


class DB:
    def __init__(self):
        self._tm = None

    def insert(self):
        print("Inserting the execution begin status in the Database")
        time.sleep(1)
        # Following code is to simulate a communication from DB to TC
        import random
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("Updating the test results in Database")
        time.sleep(1)

    def set_tm(self, tm):
        self._tm = tm


class TestManager:
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepare_reporting(self):
        r_value = self._db.insert()
        if r_value == -1:
            self._tc.set_problem(1)
            self._reporter.prepare()

    def set_reporter(self, reporter):
        self._reporter = reporter

    def set_db(self, db):
        self._db = db

    def publish_reporter(self):
        self._db.update()
        r_value = self._reporter.report()

    def set_tc(self, tc):
        self._tc = tc


if __name__ == "__main__":
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.set_reporter(reporter)
    tm.set_db(db)

    reporter.set_tm(tm)
    db.set_tm(tm)

    # For simplification, we are looping on the same test.
    # Practically, it could be about various unique test classes and their objects
    while (True):
        tc = TC()
        tc.set_tm(tm)
        tm.set_tc(tc)
        tc.setup()
        tc.execute()
        tc.tear_down()
    