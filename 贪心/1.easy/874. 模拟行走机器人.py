from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.position = [0,0]   #位置
        self.face = 0
        #[0, 1, 2, 3] 四个方向 顺时针 北 东 南 西
        self.obstacles = set(map(tuple,obstacles))
        result = 0
        hold = False
        for i,command in enumerate(commands):
            if command < 0:
                #判断方向
                self.judgeFace(command)
                hold = False
            else:
                if not hold:
                    #判断障碍物
                    if self.judgeObstacle(command):
                        hold = True
                        if self.face == 0:
                            self.position[1] = self.obstacle - 1
                        elif self.face == 1:
                            self.position[0] = self.obstacle - 1
                        elif self.face == 2:
                            self.position[1] = self.obstacle + 1
                        elif self.face == 3:
                            self.position[0] = self.obstacle + 1
                    else:
                        if self.face == 0:
                            self.position[1] += command
                        elif self.face == 1:
                            self.position[0] += command
                        elif self.face == 2:
                            self.position[1] -= command
                        elif self.face == 3:
                            self.position[0] -= command
                #print(self.position, command, result, self.face)
                if i == len(commands) - 1 or commands[i+1] < 0:
                    new_result = self.position[0]*self.position[0] + self.position[1]*self.position[1]
                    if result < new_result:
                        result = new_result
        return result
    def judgeFace(self, command):
        if command == -1:
            #向右转
            self.face = (self.face+1)%4
        else:
            #向左转
            self.face = (self.face-1)%4

    def judgeObstacle(self, distance):
        obstacles = []
        if self.face == 0:
            #找出与机器人x值相同的障碍物坐标排序找出最近的
            for obstacle in self.obstacles:
                if obstacle[0] == self.position[0]:
                    obstacles.append(obstacle[1])
            obstacles.sort()
            if len(obstacles) == 0:
                return False
            else:
                #找到介于之间的位置
                for i, obstacle in enumerate(obstacles):
                    if obstacle < self.position[1]:
                        continue
                    break
                if obstacles[i] <= self.position[1] + distance and obstacles[i] > self.position[1]:
                    self.obstacle = obstacles[i]
                    return True
                else:
                    return False
        elif self.face == 1:
            for obstacle in self.obstacles:
                if obstacle[1] == self.position[1]:
                    obstacles.append(obstacle[0])
            obstacles.sort()
            if len(obstacles) == 0:
                return False
            else:
                for i,obstacle in enumerate(obstacles):
                    if obstacle < self.position[0]:
                        continue
                    break
                if obstacles[i] <= self.position[0] + distance and obstacles[i] > self.position[0]:
                    self.obstacle = obstacles[i]
                    return True
                else:
                    return False
        elif self.face == 2:
            for obstacle in self.obstacles:
                if obstacle[0] == self.position[0]:
                    obstacles.append(obstacle[1])
            obstacles.sort(reverse=True)
            if len(obstacles) == 0:
                return False
            else:
                for i, obstacle in enumerate(obstacles):
                    if obstacle > self.position[1]:
                        continue
                    break
                if obstacles[i] >= self.position[1] - distance and obstacles[i] < self.position[1]:
                    self.obstacle = obstacles[i]
                    return True
                else:
                    return False
        elif self.face == 3:
            for obstacle in self.obstacles:
                if obstacle[1] == self.position[1]:
                    obstacles.append(obstacle[0])
            obstacles.sort(reverse=True)
            if len(obstacles) == 0:
                return False
            else:
                for i,obstacle in enumerate(obstacles):
                    if obstacle > self.position[0]:
                        continue
                    break
                if obstacles[i] >= self.position[0] - distance and obstacles[i] < self.position[0]:
                    self.obstacle = obstacles[i]
                    return True
                else:
                    return False

commands = [3,-1,-1,-1,4,1,1,-1,-1,-2,-2,6,2,5,8,-1,6,-2,6,-2,-1,-2,5,3,-1,7,7,1,5,-1,1,-2,-2,2,2,4,6,-1,-2,1,-2,-1,4,3,6,9,-2,-2,6,-2,4,3,-2,-1,-2,3,4,2,-2,-1,-2,-2,-1,5,5,8,5,2,5,4,8,-1,9,3,-1,5,-1,8,1,7,8,-2,5,8,6,-1,4,2,6,-1,8,6,1,-1,3,3,-1,7,4,-1]
obstacles = [[-42,30],[45,17],[91,15],[79,-50],[-56,-6],[-75,85],[-60,71],[37,-49],[68,-83],[38,56],[-76,95],[-77,15],[-61,48],[100,15],[-29,-60],[-44,-33],[30,4],[-43,-18],[-65,96],[71,-33],[63,-71],[-41,34],[66,-53],[53,-88],[-74,10],[-75,-79],[2,-12],[100,-60],[-94,-6],[52,-73],[-43,-43],[-1,-38],[-19,54],[-55,89],[-57,2],[-59,48],[44,67],[-58,-87],[-55,-1],[-24,-86],[71,-38],[-31,45],[72,66],[-79,30],[81,-29],[-35,81],[31,91],[-64,56],[-72,-36],[86,31],[17,-71],[76,27],[4,30],[54,-88],[-52,79],[80,0],[77,29],[14,-39],[-32,-29],[-81,77],[10,18],[56,51],[35,54],[-1,-65],[-24,-69],[-77,-76],[-71,78],[76,-91],[80,-84],[24,96],[-20,57],[-38,-56],[-85,40],[14,96],[-19,0],[-22,-97],[-86,-31],[43,-93],[-61,-20],[42,97],[0,-19],[27,-93],[80,94],[35,46],[-86,-47],[-85,-69],[47,71],[-93,40],[6,88],[45,-34],[-8,79],[19,81],[55,-39],[-78,-90],[-49,20],[30,-37],[14,-16],[84,-47],[61,-92],[71,-26],[-4,72],[23,72],[-40,96],[-22,78],[19,22],[69,84],[-30,-44],[-78,-46],[-77,29],[20,-15],[-14,12],[-5,-92],[57,-91],[-10,-55],[74,17],[58,-72],[-11,96],[-62,-38],[24,-4],[1,-30],[-89,89],[19,45],[-77,-79],[-69,-95],[-21,-80],[-49,41],[51,15],[90,88],[14,-8],[-38,-50],[91,-91],[63,-49],[-69,-72],[-92,-12],[37,32],[67,84],[3,-5],[-96,84],[-47,-37],[-41,-41],[-83,30],[-4,-4],[-55,9],[-47,50],[99,-93],[-100,17],[97,-64],[36,-72],[1,-100],[-41,-84],[81,3],[-87,-52],[58,93],[71,3],[28,40],[-93,-53],[55,9],[-82,90],[37,60],[-33,-28],[39,-21],[-12,79],[-29,9],[4,-6],[75,-9],[31,43],[-26,-35],[24,89],[-37,-55],[33,-15],[-17,-8],[-3,-89],[-85,5],[25,-83],[34,59],[22,11],[72,35],[-40,-51],[-25,-85],[-17,73],[-53,-45],[-75,32],[91,-67],[-90,19],[-38,-96],[52,8],[-5,20],[39,-38],[90,90],[-14,69],[63,85],[-71,37],[-16,-7],[-52,8],[60,84],[15,3],[1,42],[-27,-58],[-88,57],[27,-24]]
print(Solution().robotSim(commands, obstacles ))


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x = y = di = res = 0
        obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:
                di = (di - 1) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]

                        res = max(res, x * x + y * y)
        return res

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        n=len(commands)
        if n<1:
            return 0
        newobstacles=set([tuple(i) for i in obstacles])#用set存储obstacles
        if (0,0) in newobstacles:#排除起点有障碍的情况,直接去除这个障碍,不影响后续操作
            newobstacles.remove((0,0))
        x,y=0,0
        direction=[(0,1),(1,0),(0,-1),(-1,0)]#上左下右
        curdirection=(0,1)#初始方向向北
        res=0
        for command in commands:
            if command==-1:
                temp=direction.index(curdirection)
                curdirection=direction[(temp+1)%4]#每次向右转,方向就转向下一个状态
            elif command==-2:
                temp=direction[::-1].index(curdirection)
                curdirection=direction[::-1][(temp+1)%4]#向左转则,与上面相反即可
            else:
                newx=x+command*curdirection[0]
                newy=y+command*curdirection[1]#先假设没有障碍时,当前能到达的位置
                if obstacles:
                    if newx==x:#x相等,去y轴从小到大遍历
                        for tempy in range(min(y,newy),max(y,newy)+1):
                            if (x,tempy) in newobstacles:
                                newy=tempy-curdirection[1]#若有障碍,则退回一步,即与原来方向相反的走一步
                                break;
                    else:
                        for tempx in range(min(x,newx),max(x,newx)+1):
                            if (tempx,y) in newobstacles:
                                newx=tempx-curdirection[0]
                                break;
                x,y=newx,newy#每次有新的位置点产生时,计算欧式距离
                #print(newx,newy,command)
                res=max(res,x**2+y**2)
        return res
print('-'*20)
print(Solution().robotSim(commands, obstacles))