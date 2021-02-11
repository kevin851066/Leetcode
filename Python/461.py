class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        :type: x: int
        :type: y: int
        :rtype: int
        '''
        result = x ^ y
        code = self.convertbinary(result)
        return code.count('1')
        
    def convertbinary(self, i):
        code = ''
        while i > 0:
            code += str(i % 2)
            i //= 2
        return code[::-1]
