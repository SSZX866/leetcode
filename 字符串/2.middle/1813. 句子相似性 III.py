# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 22:35
# @File    : 1813. 句子相似性 III.py
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(' '), sentence2.split(' ')
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        # print(s1,s2)
        for each in s2:
            if each not in s1:
                return False
        index, flag = 0, False
        if len(s2) == 1:
            if s1.index(s2[0]) == 0 or s1.index(s2[0]) == len(s1)-1:
                return True
            else:
                return False
        for i, each in enumerate(s2):
            # print(s1,each,flag)
            try:
                if s1.index(each) != 0 and flag:
                    return False
                elif s1.index(each) != 0:
                    s1 = s1[s1.index(each) + 1:]
                    flag = True
                else:
                    s1 = s1[1:]
            except:
                return False
            # print(s1,111)
        if s1 != []:
            return False
        return True


if __name__ == '__main__':
    sentence1 = "My name is Haley"
    sentence2 = "Haley"

    print(Solution().areSentencesSimilar(sentence1, sentence2))
