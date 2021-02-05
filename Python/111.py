# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def calHeight(node):
    if node == None:
        return 0
    else:
        lheight = calHeight(node.left)
        rheight = calHeight(node.right)
        if 0 in [lheight, rheight]:
            return max(lheight+1, rheight+1)
        else:
            return min(lheight+1, rheight+1)
        
class Solution:
    def minDepth(self, root):
        '''
        : type: root: TreeNode
        : rtype: int
        '''
        return calHeight(root)