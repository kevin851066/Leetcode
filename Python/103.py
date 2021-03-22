# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        '''
        :type: root: TreeNode
        :rtype: List[List[int]]
        '''
        s, tmp, res, flag = [root], [], [], 1
        if root:
            while s:
                for _ in range(len(s)):
                    node = s.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        s.append(node.left)
                    if node.right:
                        s.append(node.right)
                res.append(tmp[::flag])
                tmp = []
                flag *= -1
            return res
        else:
            return res