class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        i = 0
        while k != 0:
            if num[i] > num[i+1]:
                num = str(int(num[:i]+num[i+1:]))
                k -= 1
                if i != 0:
                    i -= 1 #回朔 防止 999876123这种情况
            else:
                i += 1
            print(i, k, num)
            if i == len(num)-1:
                if num[i] > num[i - 1]:
                    if num[:i-k+1] == '':
                        return '0'
                    else:
                        return num[:i-k+1]
                else:
                    if num[k-i-1:] == '':
                        return '0'
                    else:
                        return num[k-i-1:]
        if num == '':
            return '0'
        else:
            return num

if __name__ == '__main__':
    num = "5337"
    k = 2
    print(Solution().removeKdigits(num, k))


# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         numStack = []
#
#         # 构建单调递增的数字串
#         for digit in num:
#             while k and numStack and numStack[-1] > digit:
#                 numStack.pop()
#                 k -= 1
#
#             numStack.append(digit)
#
#         # 如果 K > 0，删除末尾的 K 个字符
#         finalStack = numStack[:-k] if k else numStack
#
#         # 抹去前导零
#         return "".join(finalStack).lstrip('0') or "0"