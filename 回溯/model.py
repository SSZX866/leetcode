# 回溯的中心思想是，当我们遇到求问题的所有有效的解决方案时，
# 要对所有可能的方案进行尝试，再不断的尝试过程中寻找问题的解，
# 如果当前不是解则返回上一层去尝试其他方案。

# 根据上面的理解大致思路是，每次去探索一条路径上的解决方案时候，
# 回溯返回上一层针对的是当前路径，对当前路径下未探索的路径有一下两种情况
# 1.当前未搜索区域满足结束条件，则保存当前路径并退出当前搜索；
# 2.当前未搜索区域需要继续搜索，则遍历当前所有可能的选择：
# 如果该选择符合要求，则把当前选择加入当前的搜索路径中，并继续搜索新的未探索区域
# 如下模板：

# res = []
# path = []
#
# def backtrack(未探索区域, res, path):
#     if path 满足条件:
#         res.add(path) # 深度拷贝
#         # return  # 如果不用继续搜索需要 return
#     for 选择 in 未探索区域当前可能的选择:
#         if 当前选择符合要求:
#             path.add(当前选择)
#             backtrack(新的未探索区域, res, path)
#             path.pop()

# backtrack代表的意思是所有未探索可能到达结束条件的路径，res保存的是已经探索到的路径，
# path代表保存的一条路径，所以当「未探索区域满足结束条件」时，需要把 path 放到结果 res 中。
# path.pop() 是啥意思呢？它是编程实现上的一个要求，即我们从始至终只用了一个变量 path，
# 所以当对 path 增加一个选择并 backtrack 之后，需要清除当前的选择，防止影响其他路径的搜索。
