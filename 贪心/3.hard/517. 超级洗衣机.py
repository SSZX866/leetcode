# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 09:41
# @File    : 517. 超级洗衣机.py
from leetcode import *

# 有四个洗衣机，装的衣服数为[0, 0, 11, 5]，最终的状态会变为[4, 4, 4, 4]，
# 那么我们将二者做差，得到[-4, -4, 7, 1]，这里负数表示当前洗衣机还需要的衣服数，
# 正数表示当前洗衣机多余的衣服数。我们要做的是*要将这个差值数组每一项都变为0，对于第一个洗衣机来说，
# 需要四件衣服可以从第二个洗衣机获得，那么就可以 把-4移给二号洗衣机，那么差值数组变为[0, -8, 7, 1]，
# 此时二号洗衣机需要八件衣服，那么至少需要移动8次。然后二号洗衣机把这八件衣服从三号洗衣机处获得，
# 那么差值数组变为[0, 0, -1, 1]，此时三号洗衣机还缺1件，就从四号洗衣机处获得，
# 此时差值数组成功变为了[0, 0, 0, 0]，成功。那么移动的最大次数就是差值 数组中出现的绝对值最大的数字，8次

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        if s % len(machines) != 0: return -1
        balance = s // len(machines)
        deltas = [each - balance for each in machines]
        ans = max(deltas)
        for i in range(len(deltas) - 1):
            ans = max(ans, abs(deltas[i]))
            deltas[i + 1] += deltas[i]
            # deltas[i] = 0

        return ans