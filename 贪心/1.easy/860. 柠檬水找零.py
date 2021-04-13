from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            else:
                #优先使用大额bill
                if ten > 0:
                    five -= 1
                    ten -= 1
                else:
                    five -= 3
            if five < 0 or ten < 0 or twenty < 0:
                return False
        return True

if __name__ == '__main__':
    print(Solution().lemonadeChange([5,5,10,10,20]))