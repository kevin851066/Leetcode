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
    def connect(self, root: 'Node') -> 'Node': # find all existed nodes in same level and link them
        if root:
            s = [root]
            while s:
                layer_nodes = []
                for i in range(len(s)):
                    if s[i].left:
                        layer_nodes.append(s[i].left)
                    if s[i].right:
                        layer_nodes.append(s[i].right)
                for i in range(len(layer_nodes)-1):
                    layer_nodes[i].next = layer_nodes[i+1]
                s = layer_nodes
        return root