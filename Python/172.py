class Solution1:
    def trailingZeroes(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res

class Solution2:
    def trailingZeroes(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n+1):
            while i % 5 == 0:
                i //= 5
                res += 1
        return res

class Solution3:
    def trailingZeroes(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        fac = 1 
        for i in range(1, n+1):
            fac *= i
        fac = str(fac)
        
        res = 0
        for i in fac[::-1]:
            if i != '0':
                break
            else:
                res += 1
        return res


        