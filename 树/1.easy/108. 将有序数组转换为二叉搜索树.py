from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         self.i = 0
#         root = TreeNode()
#         queue = [root]
#         i = 0
#         while True:
#             node = queue.pop(0)
#             if i == len(nums):
#                 break
#             else:
#                 node.left = TreeNode()
#                 queue.append(node.left)
#                 i += 1
#             if i == len(nums):
#                 break
#             else:
#                 node.right = TreeNode()
#                 queue.append(node.left)
#                 i += 1
#         self.nums = nums
#         self.inorder(root)
#         return root
#     def inorder(self, node):
#         if not node:
#             return
#         self.inorder(node.left)
#         if self.i > 3:
#             return
#         print(self.i)
#         node.val = self.nums[self.i]
#         self.i += 1
#         self.inorder(node.right)


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         length = len(nums)
#         i = length // 2
#         root = TreeNode(val=nums[i])
#         if length >= 2:
#             root.left = TreeNode(val=nums[i-1])
#         if length >= 3:
#             root.right = TreeNode(val=nums[-1])
#         if length >= 4:
#             l = 1
#             i -= 1
#             left_node, right_node = root.left, root.right
#             left_node.left = TreeNode(val=nums[i - 1])
#             right_node.left = TreeNode(val=nums[length - l - 1])
#             i -= 1
#             l += 1
#             while i > 0:
#                 left_node, right_node = left_node.left, right_node.left
#                 left_node.left = TreeNode(val=nums[i-1])
#                 right_node.left = TreeNode(val=nums[length-l-1])
#                 i -= 1
#                 l += 1
#             if length%2 == 0:
#                 right_node.left = None
#         return root

if __name__ == '__main__':
    nums = [-1,0,1,2]
    print(Solution().sortedArrayToBST(nums))

