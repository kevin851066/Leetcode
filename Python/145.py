# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root):
        '''
        :type: root: TreeNode
        :rtype: List[int]
        '''
        res = []
        if root == None:
            return root        
        else:
            self.dfs(root, res)
            return res
        
    def dfs(self, node, res):
        if node.left:
            self.dfs(node.left, res)
        if node.right:
            self.dfs(node.right, res)  
        res.append(node.val)