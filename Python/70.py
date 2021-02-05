class Solution:
    def climbStairs(self, n):
         """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            s = []
            s.append(1)
            s.append(2)
            for i in range(2, n):
                s.append(s[i-1] + s[i-2])
            return s[n-1]

