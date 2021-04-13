from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(x[0],-x[1]),reverse=True)
        queue = []
        for each in people:
            queue.insert(each[1],each)
            #queue[each[1]:each[1]] = [each] 这样写效率更高
        return queue


if __name__ == '__main__':
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(Solution().reconstructQueue(people))