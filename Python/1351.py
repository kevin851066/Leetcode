class Solution:
    def countNegatives(self, grid):
        '''
        :type: grid: List[List[int]]
        :rtype: int
        '''
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    res.append(j)
                    break
                if j == n - 1 and grid[i][j] >= 0:
                    res.append(n)
            if len(res) < i+1:
                res.append(0)
        return m * n - sum(res)

    def countNegatives2(self, grid):
        '''
        :type: grid: List[List[int]]
        :rtype: int
        '''
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        res = 0
        while i >= 0 and j < n:
            if grid[i][j] < 0:
                res += n - j
                i -= 1
            else:
                j += 1
        return res