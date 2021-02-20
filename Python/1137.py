class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        :type: n: int
        :rtype: int
        '''
        a = [0, 1, 1]
        for i in range(3, n+1):
            a.append(a[i-1]+a[i-2]+a[i-3])
        return a[n]