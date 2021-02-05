# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        '''
        : type: p: TreeNode
                q: TreeNode
        : rtype: bool
        '''
        if p == None and q == None:
            return True
        elif p ==  None or q == None:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val   