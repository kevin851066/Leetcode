class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        :type: n: int
        :rtype: bool
        '''
        return n > 0 and bin(n).count('1') == 1 and n & 1431655765 == n # bin(1431655765) = 10101...101 (31 bits)
        