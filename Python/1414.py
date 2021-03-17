class Solution:
    def findMinFibonacciNumbers(self, k):
        '''
        :type: k: int
        :rtype: int
        '''
        f = [1,1]       
        while f[-1] <= k:
            f.append(f[-1]+f[-2])
        res = 0
        i = len(f) - 1
        while i != 0:
            if k - f[i] == 0:
                res += 1
                break
            elif k - f[i] > 0:
                res += 1
                k -= f[i]
            else:
                i -= 1
        return res