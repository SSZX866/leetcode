# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 09:36
# @File    : 208. 实现 Trie (前缀树).py
class TrieNode():
    def __init__(self, val=None):
        self.val = val
        self.next = []
        self.isStr = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.startNode = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nextNode = self.startNode
        for char in word:
            nextNode = self.insertChar(char, nextNode)
        nextNode.isStr = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nextNode, i = self.startNode, 0
        while i < len(word):
            pre = i
            for node in nextNode.next:
                if node.val == word[i]:
                    i += 1
                    if i == len(word):
                        return node.isStr
                    nextNode = node
                    break
            if i == pre:
                return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nextNode, i = self.startNode, 0
        while i < len(prefix):
            pre = i
            for node in nextNode.next:
                if node.val == prefix[i]:
                    i += 1
                    nextNode = node
                    break
                if i == len(prefix): return True
            if i == pre: return False
        return True

    def insertChar(self, char: str, node: TrieNode) -> TrieNode:
        for eachNode in node.next:
            if eachNode.val == char:
                return eachNode
        node.next.append(TrieNode(char))
        return node.next[-1]


if __name__ == '__main__':
    # obj = Trie()
    # obj.insert("apple")
    # param_2 = obj.search("apple")
    # param_3 = obj.search("app")
    # param_4 = obj.startsWith("app")
    # obj.insert("app")
    # param_5 = obj.search("app")
    # print(param_2, param_3, param_4, param_5)
    obj = Trie()
    obj.insert("nemathelminth")
    obj.insert("entracte")
    param_2 = obj.search("nemathelminth")
    param_3 = obj.search("entracte")

    print(param_2, param_3)
