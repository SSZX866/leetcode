# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 15:36
# @File    : 2. 乐团站位.py
class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        boundary = [[0, 0], [num - 1, num - 1]]
        face = 1  # 0,1,2,3 分别代表北东南西
        k = 0
        i, j = 0, 0
        for _ in range(num * num):
            k = (k + 1) % 10
            if k == 0: k += 1
            # 更新face
            if i > boundary[1][0] or j > boundary[1][1] or i < boundary[0][0] or j < boundary[0][1]:
                # print(i,j,boundary)
                face = (face + 1) % 4
                # 更新boundary, 纠正i,j
                if face == 0:
                    boundary[1][0] -= 1
                    j += 1
                    i -= 1
                elif face == 1:
                    boundary[0][1] += 1
                    i += 1
                    j += 1
                elif face == 2:
                    boundary[0][0] += 1
                    j -= 1
                    i += 1
                else:
                    boundary[1][1] -= 1
                    i -= 1
                    j -= 1
            # print(i, j, face, result,boundary)

            if i == xPos and j == yPos:
                return k
            # 更新i, j
            if face == 0:
                i -= 1
            elif face == 1:
                j += 1
            elif face == 2:
                i += 1
            else:
                j -= 1


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        num -= 1
        xPos, yPos = yPos, xPos  # x,y搞反了
        layer = min(min(xPos, num - xPos), min(yPos, num - yPos), num - min(xPos, num - xPos),
                    num - min(yPos, num - yPos))
        offset = 0
        if yPos == layer:
            offset = xPos - layer + 1
        else:
            if xPos >= yPos:
                offset = (num + 1 - (layer) * 2) + yPos - layer
            else:
                offset += (num + 1 - (layer) * 2) * 2 - 1
                if yPos == layer + (num + 1 - (layer) * 2) - 1:
                    offset += yPos - xPos
                else:
                    offset += (num + 1 - (layer) * 2) + layer + (num + 1 - (layer) * 2) - yPos - 2
        # print(layer, offset)
        ans = pow((num + 1), 2) - pow((num + 1 - (layer) * 2), 2) + offset
        return (ans - 1) % 9 + 1


if __name__ == '__main__':
    num = 5
    Xpos = 0
    Ypos = 2
    print(Solution().orchestraLayout(num, Xpos, Ypos))
