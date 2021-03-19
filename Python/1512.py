import collections

class Solution:
    def numIdenticalPairs(self, nums):
        '''
        :type: nums: List[int]
        :rtype: int
        '''
        c = collections.Counter(nums)
        res = 0
        for ele in c:
            if c[ele] > 1:
                res += self.combination(c[ele])
        return int(res)
    
    def combination(self, n):
        return  self.factorial(n) / (self.factorial(n-2) * 2)
    
    def factorial(self, m):
        if m == 1 or m == 0:
            return 1
        if m >= 2:
            return m * self.factorial(m-1) 