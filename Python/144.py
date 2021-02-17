# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root):
        '''
        :type: root: TreeNode
        :rtype: List[int]
        '''
        if root:
            res = []
            self.dfs(root, res)
            return res
        else:
            return []
        
    def dfs(self, node, res):
        res.append(node.val)
        if node.left:
            self.dfs(node.left, res)
        if node.right:
            self.dfs(node.right, res)
                    