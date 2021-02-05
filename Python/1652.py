class Solution:
    def decrypt(self, code, k):
        '''
        type: code: List[int]
        type: k: int
        rtype: List[int]
        '''
        output = []
        if k == 0:
            return [0] * len(code)
        else:
            circode = code + code
            for i in range(len(code)):
                s = 0
                if k > 0:
                    for j in range(k):
                        s += circode[i+j+1]
                else:
                    for j in range(abs(k)):
                        s += circode[i+ j + len(code) + k]
                output.append(s)
        return output