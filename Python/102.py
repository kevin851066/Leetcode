import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        '''
        :root: TreeNode
        :rtype: List[List[int]]
        '''
        q, res = collections.deque(), []
        if root:
            res.append([root.val])
            q.append((root, 0)) # 0: level 0
            while q:
                node, level = q.popleft()
                level += 1
                if node.left or node.right:
                    if len(res) < level + 1:
                        res.append([])
                    if node.left:
                        res[level].append(node.left.val)
                        q.append((node.left, level))
                    if node.right:
                        res[level].append(node.right.val)
                        q.append((node.right, level))
        return res