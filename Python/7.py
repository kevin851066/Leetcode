class Solution:
    def reverse(self, x):
        '''
        : type: x: int
        : rtype: int
        '''
        result = 0
        flag = False
        if x < 0:
            x *= (-1)
            flag = True
        while x != 0:
            r = x % 10
            x = x // 10
            result = 10 * result + r
            if result < (-1) * 2 ** 31 or result > 2 ** 31 - 1:
                return 0
        if flag:
            result *= (-1)
        
        return result
            