# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 14:30
# @File    : 1114. 按序打印.py
class Foo:
    def __init__(self):
        self.f = False
        self.s = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.f: pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.s: pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
