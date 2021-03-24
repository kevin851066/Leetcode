"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        :type: root: 'Node'
        :rtype: 'Node'
        '''
        if root:
            s = [root]
            while s:
                node = s.pop(0)
                if node.left:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
                    s.append(node.left)
                    s.append(node.right)
            return root 
            
        