# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def averageOfLevels(self, root):
        '''
        :type: root: TreeNode
        :rtype: List[float]
        '''
        output = []
        q = collections.deque([(root, 0)]) # 0: level
        while q:
            (node, level) = q.popleft()
            if len(output) < level + 1:
                output.append([])
            output[level].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return [mean(level) for level in output]