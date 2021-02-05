# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def calHeight(node):
    if node != None:
        lheight = calHeight(node.left)
        rheight = calHeight(node.right)
        if lheight == -1 or rheight == -1:
            return -1
        if abs(lheight - rheight) > 1:
            return -1
        else:
            return max(lheight+1, rheight+1)
    else:
        return 0

class Solution:
    def isBalanced(self, root):
        '''
        : type: root: TreeNode
        : rtype: bool
        '''
        if root!= None:
            if calHeight(root) == -1:
                return False
            else:
                return True
        else:
            return True