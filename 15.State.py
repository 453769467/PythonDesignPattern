# -*- coding: UTF-8 -*-
"""
状态模式（State）
模式说明：
    ---

意图：
    允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。

适用性：
    1. 一个对象的行为取决于它的状态, 并且它必须在运行时刻根据状态改变它的行为。
    2.  一个操作中含有庞大的多分支的条件语句，且这些分支依赖于该对象的状态, 这个状态通常用一个或多个枚举常量表示, 通常,
        有多个操作包含这一相同的条件结构

优点：
    ---
缺点：
    ---

"""


class State(object):
    """
    基本状态，这是为了共享功能
    """
    def scan(self):
        """
        扫描下一个状态
        :return:
        """
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0

        print("Scanning... Station is", self.stations[self.pos], self.name)


class AMState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_am_fm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fm_state


class FMState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_am_fm(self):
        print("Switching to AM")
        self.radio.state = self.radio.am_state


class Radio(object):
    """
    A radio.
    It has a scan button, and an AM/FM toggle switch.
    """
    def __init__(self):
        """
        We have an AM state and an FM state
        """
        self.am_state = AMState(self)
        self.fm_state = FMState(self)
        self.state = self.am_state

    def toggle_am_fm(self):
        self.state.toggle_am_fm()

    def scan(self):
        self.state.scan()


if __name__ == "__main__":
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_am_fm] + [radio.scan] *2
    actions = actions * 2

    for action in actions:
        action()
    