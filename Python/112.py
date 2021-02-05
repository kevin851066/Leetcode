# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def checkleaf(node, remain):
    if node != None:
        if not node.left and not node.right: # leaf
            if remain - node.val == 0:
                return True
            else:
                return False
        else: # at least one sub-tree
            return checkleaf(node.left, remain-node.val) or checkleaf(node.right, remain-node.val)
    
class Solution:
    def hasPathSum(self, root, targetSum):
        '''
        : type: root: TreeNode
                targetSum: int
        : rtype: bool
        '''
        return checkleaf(root, targetSum)