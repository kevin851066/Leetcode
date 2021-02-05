# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def CHeckLR(lnode, rnode):
        if lnode == None and rnode == None:
            return True
        elif lnode == None or rnode == None:
            return False
        else:
            return lnode.val == rnode.val and CHeckLR(lnode.left, rnode.right) and CHeckLR(lnode.right, rnode.left)
        
class Solution:
    '''
    : type: root: TreeNode
    : rtype: bool
    '''
    def isSymmetric(self, root):
        if root == None:
            return True
        return CHeckLR(root.left, root.right)