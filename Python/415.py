class Solution:
    def addStrings(self, num1, num2):
        '''
        :type: num1: str
        :type: num2: str
        :rtype: str
        '''
        num1, num2 = num1[::-1], num2[::-1]
        l1, l2 = len(num1), len(num2)
        m = max(l1, l2)
        i, carry, res = 0, 0, 0
        while i < m or carry:
            d1 = ord(num1[i]) - ord('0') if i < l1 else 0
            d2 = ord(num2[i]) - ord('0') if i < l2 else 0
            
            res = res + (d1 + d2 + carry) % 10 * 10 ** i
            carry = (d1 + d2 + carry) // 10
            i += 1
            
        return str(res)