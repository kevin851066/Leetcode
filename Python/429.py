"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

import collections

class Solution:
    def levelOrder(self, root):
        '''
        :type: root: 'Node'
        :rtype: List[List[int]]
        '''
        if root == None:
            return []
        output = []
        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if len(output) < level + 1:
                output.append([])
            for c in node.children:
                q.append((c, level+1))
            output[level].append(node.val) 
        return output