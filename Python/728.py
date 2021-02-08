class Solution:
    def selfDividingNumbers(self, left, right):
        '''
        type: left: int
        type: right: int
        rtype: List[int]
        '''
        output = []
        for t in range(left, right+1):
            n = t
            isTarget = True
            while n > 0:
                rsd = n % 10 
                if rsd == 0:
                    isTarget = False
                    break
                if t % rsd != 0:
                    isTarget = False
                    break
                n //= 10 # 整除
            if isTarget:
                output.append(t)
        return output
            