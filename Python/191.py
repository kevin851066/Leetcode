class Solution:
    def hammingWeight(self, n: int):
        '''
        : type: n: int
        : rtype: int
        '''
        count = 0
        for i in range(32):
            count += (n & 1)
            n >>= 1
        return count