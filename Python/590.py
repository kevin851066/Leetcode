"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# recursive
class Solution1:
    def postorder(self, root):
        '''
        :type: root: 'Node'
        :rtype: List[int]
        '''
        res = []
        if root:
            self.dfs(root, res)
        return res
        
    def dfs(self, node, res):
        for c in node.children:
            self.dfs(c, res)
        res.append(node.val)

# iterative
class Solution2:
    def postorder(self, root):
        '''
        :type: root: 'Node'
        :rtype: List[int]
        '''
        if root == None:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]
