class Solution:
    def grayCode(self, n: int):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        if n == 0:
            return res
        for i in range(n):  # n > 0
            res += [r+2**i for r in res][::-1] 
        return res