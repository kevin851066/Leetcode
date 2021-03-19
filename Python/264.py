class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        :type: n: int
        :rtype: int
        '''
        u = [1]
        i2, i3, i5 = 0, 0, 0
        i = 1
        while i < n:
            u2, u3, u5 = 2 * u[i2], 3 * u[i3], 5 * u[i5]
            m = min(u2, u3, u5)
            if u2 == m:
                i2 += 1
            if u3 == m:
                i3 += 1
            if u5 == m:
                i5 += 1
            i += 1
            u.append(m)
        return u[-1]