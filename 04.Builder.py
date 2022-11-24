# -*- coding: UTF-8 -*-
"""
创建者模式（Builder）
模式说明：
    将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示

意图：
    将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示

适用性：
    1. 当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时
    2. 当构造过程必须允许被构造的对象有不同的表示时

基本思想:
    1. 某类产品的构建由很多复杂组件组成
    2. 这些组件中的某些细节不同，构建出的产品表象会略有不同
    3. 通过一个指挥者按照产品的创建步骤来一步步执行产品的创建
    4. 当需要创建不同的产品时，只需要派生一个具体的建造者，重写相应的组件构建方法即可
优点：
    ---
缺点：
    ---

personBuilder（父类 or 基类）
PersonFatBuilder(personBuilder的子类 or派生类）：作用为创建一个胖子的身体部位
PersonThinBuilder(personBuilder的子类 or派生类）：作用为创建一个瘦子的身体部位
PersonDirector（新式类）：作用为根据personBuilder子类对象（如PersonFatBuilder()）让其创建其身体部位
"""


def print_info(info):
    print(info)


class PersonBuilder():
    """
    建造者基类
    """
    def build_head(self):
        pass

    def build_body(self):
        pass

    def build_arm(self):
        pass

    def build_leg(self):
        pass


class PersonFatBuilder(PersonBuilder):
    """
    胖子
    """
    type = "胖子"

    def build_head(self):
        print_info("构建%s的大。。。。。头" % self.type)

    def build_body(self):
        print_info("构建%s的身体" % self.type)

    def build_arm(self):
        print_info("构建%s的手" % self.type)

    def build_leg(self):
        print_info("构建%s的脚" % self.type)


class PersonThinBuilder(PersonBuilder):
    """
    瘦子
    """
    type = "瘦子"

    def build_head(self):
        print_info("构建%s的大。。。。。头" % self.type)

    def build_body(self):
        print_info("构建%s的身体" % self.type)

    def build_arm(self):
        print_info("构建%s的手" % self.type)

    def build_leg(self):
        print_info("构建%s的脚" % self.type)


class PersonDirector():
    """
    指挥者
    """
    person_builder = None

    def __init__(self, person_builder):
        self.person_builder = person_builder

    def create_person(self):
        self.person_builder.build_head()
        self.person_builder.build_body()
        self.person_builder.build_arm()
        self.person_builder.build_leg()


def client_ui():
    thin_person_builder = PersonThinBuilder()
    thin_person_director = PersonDirector(thin_person_builder)
    thin_person_director.create_person()

    fat_person_builder = PersonThinBuilder()
    fat_person_director = PersonDirector(fat_person_builder)
    fat_person_director.create_person()

    return


if __name__ == "__main__":
    client_ui()
