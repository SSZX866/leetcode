class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tree=preorder.split(',')
        if tree == ['#']:
            return True
        if len(tree) < 3:
            return False
        while tree != ['#']:
            i = 0
            mark = False
            while True:
                # print(i,length,tree)
                if tree[i].isdigit() and tree[i+1] == "#" and tree[i+2] == "#":
                    tree.pop(i)
                    tree.pop(i)
                    mark = True
                i += 1
                length = len(tree)
                if i >= length - 2:
                    break
            if not mark:
                return False
        return True

if __name__ == '__main__':
    preorder = "9,#,#,1"
    print(Solution().isValidSerialization(preorder))