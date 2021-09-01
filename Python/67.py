class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        '''
        :type: a: str
               b: str
        :rtype: str
        '''

        a = list(a) 
        b = list(b)
        res = ''
        carry = 0
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res = str(carry % 2) + res
            carry //= 2
        return res

class Solution2:  
    def addBinary(self, a: str, b: str) -> str:
        '''
        :type: a: str
               b: str
        :rtype: str
        '''
        la, lb = len(a), len(b)
        ra, rb = a[::-1], b[::-1]
        carry, idx = 0, 0
        res = ""
        while la - idx > 0 or lb - idx > 0 or carry: 
            if idx > la - 1 :
                if idx > lb - 1:
                    v = carry
                else:
                    v = int(rb[idx]) + carry
            else:
                if idx > lb - 1:
                    v = int(ra[idx]) + carry
                else:
                    v = int(ra[idx]) + int(rb[idx]) + carry
            carry = v // 2
            if carry:
                v = v % 2
            res += str(v)
            idx += 1
        return res[::-1]