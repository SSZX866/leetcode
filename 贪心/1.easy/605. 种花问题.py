from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        f_len = len(flowerbed)
        cnt = 0
        if f_len == 1:
            if n == 0:
                return True
            if n < 2:
                return n != flowerbed[0]
            else:
                return False
        while i < f_len - 1 and cnt < n:
            if flowerbed[i] == 1:
                i += 1
                continue
            if flowerbed[i+1] == 0:#找到连续两个0的情况种花
                if i+2 == f_len:#恰好为最后两个是0的情况
                    return cnt+1 >= n
                if i == 0:#需加上恰好为开头两个是0的情况
                    cnt += 1
                    i += 1
                else:
                    if flowerbed[i+2] == 0:
                       cnt += 1
                       i += 2
                    else:
                        i += 3
            else:
                i += 2
        return cnt >= n

if __name__ == '__main__':
    print(Solution().canPlaceFlowers(flowerbed = [0,0,0,0,1], n = 2))



#防御式编程思想：在 flowerbed 数组两端各增加一个 0， 这样处理的好处在于不用考虑边界条件，任意位置处只要连续出现三个 0 就可以栽上一棵花。
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        tmp = [0]+flowerbed+[0]
        for i in range(1, len(tmp)-1):
            if tmp[i-1] == 0 and tmp[i] == 0 and tmp[i+1] == 0:
                tmp[i] = 1  # 在 i 处栽上花
                n -= 1
        return n <= 0   # n 小于等于 0 ，表示可以栽完花