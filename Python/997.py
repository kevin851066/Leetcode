class Solution:
    def findJudge(self, N, trust):
        '''
        type: N: int
        type: trust: List[List[int]]
        rtype: int
        '''
        p = [0] * N
        for t in trust:
            p[t[0]-1] -= 1
            p[t[1]-1] += 1
        for i in range(len(p)):
            if p[i] == N - 1:
                return i + 1
        return -1