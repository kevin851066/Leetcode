# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def findTarget(self, root, k):
        '''
        :type: root: TreeNode
        :type: k: int
        :rtype: bool
        '''
        s = set()
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.val in s:
                return True
            else:
                s.add(k - node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
        