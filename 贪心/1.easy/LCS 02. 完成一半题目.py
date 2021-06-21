# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 15:09
# @File    : 1000080. 完成一半题目.py
from leetcode import *


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        people = len(questions) // 2
        count = Counter(questions)
        quests = [each for each in count.values()]
        quests.sort(reverse=True)
        ans = 0
        for each in quests:
            people -= each
            ans += 1
            if people <= 0: return ans


if __name__ == '__main__':
    questions = [2, 1, 6, 2]
    questions = [1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6]
    print(Solution().halfQuestions(questions))
