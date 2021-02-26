class Solution:
    def plusOne(self, digits):
        '''
        :type: digits: List[int]
        :rtype: List[int]
        '''
        digits_i, i, res = 0, 0, []
        lend = len(digits)
        
        while i < lend:
            digits_i = 10 * digits_i + digits[i]
            i += 1
            
        digits_i += 1
        for j in str(digits_i):
            res.append(j)
            
        return res
