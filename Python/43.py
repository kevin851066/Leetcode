class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        :type: num1: str
        :type: num2: str
        :rtype: str
        '''
        
        num1, num2 = num1[::-1], num2[::-1]
        res = 0
        for idx2, d2 in enumerate(num2): 
            i2 = ord(d2) - ord('0')
            for idx1, d1 in enumerate(num1):
                i1 = ord(d1) - ord('0')
                res += (i1*i2) * 10 ** (idx1 + idx2)
        return str(res)