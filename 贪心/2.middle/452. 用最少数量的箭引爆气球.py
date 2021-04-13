from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []:
            return 0
        points.sort(key=lambda x:(x[1],x[0]), reverse=True)
        section = [0,0]
        section[0], section[1] = points[0][0]+1, points[0][1]-1
        #print(points)
        #res = []
        result = 0
        for each in points:
            #print(each,section)
            if not (section[0] <= each[0] <= section[1] or section[0] <= each[1] <= section[1]):
                #res.append(each)
                result += 1
                section = each
                continue
            if section[0] <= each[0] <= section[1]:
                section[0] = each[0]
            if section[0] <= each[1] <= section[1]:
                section[1] = each[1]
            #print(section,111)
        #print(res)
        return result

if __name__ == '__main__':
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(Solution().findMinArrowShots(points))

###
###标准答案中给出不用判断左边界，因为每次都在判断左边界是否大于又边界
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda points: points[1])  # 以右边界Xend升序排列

        right_limit = points[0][1]

        n_arrow = 1

        for bolloon in points:
            if bolloon[0] > right_limit:  # 如果左边界大于了目前的最大的有边界，那么就不得不再射一只箭
                right_limit = bolloon[1]
                n_arrow += 1

        return n_arrow