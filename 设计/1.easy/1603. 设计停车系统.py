# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 9:20
# @File    : 1603. 设计停车系统.py
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.numbers = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.numbers[carType - 1] -= 1
        if self.numbers[carType - 1] < 0:
            self.numbers[carType - 1] = 0
            return False
        else:
            return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
