# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        '''
        :type: root: TreeNode
        :rtype: List[int]
        '''
        res = []
        if root == None:
            return []
        else:
            self.dfs(root, res)
            return res
            
    def dfs(self, node, res):
        if node.left:
            self.dfs(node.left, res)
        res.append(node.val)
        if node.right:
            self.dfs(node.right, res)