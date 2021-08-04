from leetcode import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree():
    def __init__(self):
        self.root = None

    def add(self, val):
        # 广度遍历（层次遍历），队列
        node = TreeNode(val)
        queue = [self.root]
        if not self.root:
            self.root = node
            return
        while True:
            # 弹出队列的第一个元素
            cur_node = queue.pop(0)
            if cur_node.left:
                queue.append(cur_node.left)
            else:
                cur_node.left = node
                break
            if cur_node.right:
                queue.append(cur_node.right)
            else:
                cur_node.right = node
                break
        return

    def breadth_travel(self):
        # 广度遍历
        queue = [self.root]
        if not self.root:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=' ')
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    def preorder(self, root):
        # 先序遍历
        if not root:
            return
        print(root.val, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        # 中序遍历
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)

    def postorder(self, root):
        # 后序遍历
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=' ')

    def preorderTraversal(self, root):
        # 迭代前序遍历
        if not root: return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return ans

    def inorderTraversal(self, root):
        # 迭代中遍历
        if not root: return []
        res, stack = [], [[root, False]]
        while stack:
            node, needAdd = stack.pop()
            if needAdd:
                res.append(node.val)
            else:
                if node.right: stack.append([node.right, False])
                stack.append([node, True])
                if node.left: stack.append([node.left, False])
        return res

    def postorderTraversal(self, root):
        # 迭代后序遍历
        if not root: return []
        res, stack = [], [[root, False]]
        while stack:
            node, needAdd = stack.pop()
            if needAdd:
                res.append(node.val)
            else:
                stack.append([node, True])
                if node.right: stack.append([node.right, False])
                if node.left: stack.append([node.left, False])
        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        # 迭代后序遍历 反转答案
        if not root: return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return ans[::-1]


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.breadth_travel()
    print(' <=breadth travel')
    tree.preorder(tree.root)
    print(' <=preorder')
    tree.inorder(tree.root)
    print(' <=inorder')
    tree.postorder(tree.root)
    print(' <=postorder')
    preorderTraversal = tree.preorderTraversal(tree.root)
    for val in preorderTraversal:
        print(val, end=' ')
    print(' <=preorderTraversal')
    inorderTraversal = tree.inorderTraversal(tree.root)
    for val in inorderTraversal:
        print(val, end=' ')
    print(' <=inorderTraversal')
    postorderTraversal = tree.postorderTraversal(tree.root)
    for val in postorderTraversal:
        print(val, end=' ')
    print(' <=postorderTraversal')
