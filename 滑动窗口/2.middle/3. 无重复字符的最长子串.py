# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 16:27
# @File    : 3. 无重复字符的最长子串.py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, dic, ans = 0, 0, {}, 0
        while j < len(s):
            dic[s[j]] = 1 if s[j] not in dic else dic[s[j]] + 1
            while dic[s[j]] > 1:
                dic[s[i]] -= 1
                i += 1
            j += 1
            ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
