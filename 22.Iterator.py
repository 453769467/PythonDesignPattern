# -*- coding: UTF-8 -*-
"""
迭代器模式（Iterator）
模式说明：
    ---

意图：
    提供一种方法顺序访问一个聚合对象中各个元素, 而又不需暴露该对象的内部表示。

适用性：
    1. 访问一个聚合对象的内容而无需暴露它的内部表示。
    2. 支持对聚合对象的多种遍历。
    3. 为遍历不同的聚合结构提供一个统一的接口(即, 支持多态迭代)。

优点：
    ---
缺点：
    ---

"""


def count_to(count):
    """
    Counts by word numbers, up to a maximum of five
    :param count:
    :return:
    """
    numbers = ["one", "two", "three", "four", "five"]
    for pos, num in zip(range(count), numbers):
        yield num


if __name__ == "__main__":
    # Test the generator
    count_to_two = count_to(2)
    count_to_five = count_to(5)

    print("Counting to two...")
    for number in count_to_two:
        print(number)

    print("--" * 8)

    print("Counting to five...")
    for number in count_to_five:
        print(number)

    print("--" * 8)
    