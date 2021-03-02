class Solution:
    def balancedStringSplit(self, s):
        '''
        :type: s: str
        :rtype: int
        '''
        l_num, r_num = 0, 0
        res = 0
        for i in s:
            if i == 'L':
                l_num += 1
            else:
                r_num += 1
            if l_num == r_num:
                res += 1
                l_num = 0
                r_num = 0
        return res
                