import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root):
        '''
        :type: root: TreeNode
        :rtype: List[List[int]]
        '''
        res, q = [], collections.deque()
        if root != None:
            q.append((root, 0))
            while q:
                node, level = q.popleft()
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                if node.left != None:
                    q.append((node.left, level + 1))
                if node.right != None:
                    q.append((node.right, level + 1))
        return res