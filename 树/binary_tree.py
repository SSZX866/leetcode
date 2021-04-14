class Node():
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        # 广度遍历（层次遍历），队列
        node = Node(item)
        queue = [self.root]
        if not self.root:
            self.root = node
            return
        while True:
            # 弹出队列的第一个元素
            cur_node = queue.pop(0)
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            else:
                cur_node.lchild = node
                break
            if cur_node.rchild:
                queue.append(cur_node.rchild)
            else:
                cur_node.rchild = node
                break
        return

    def breadth_travel(self):
        # 广度遍历
        queue = [self.root]
        if not self.root:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)

    def preorder(self, root):
        # 先序遍历
        if not root:
            return
        print(root.elem, end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        # 中序遍历
        if not root:
            return
        self.inorder(root.lchild)
        print(root.elem, end=' ')
        self.inorder(root.rchild)

    def postorder(self, root):
        # 后序遍历
        if not root:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end=' ')

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


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print(' ')
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)
