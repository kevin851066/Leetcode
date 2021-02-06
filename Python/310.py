class Solution:
    def findMinHeightTrees(self, n, edges):
        '''
        type: n: int
        type: edges: List[List[int]]
        rtype: List[int]
        '''
        if n == 1: return [0]
        g = [[] for i in range(n)]
        for v1, v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)
        
        leaves = [i for i, v in enumerate(g, 0) if len(v) == 1]
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                nxt = g[i][0] # must have only one element since its degree is 1
                g[i] = []
                g[nxt].remove(i)
                if len(g[nxt]) == 1:
                    newleaves.append(nxt)
            leaves = newleaves
        return leaves