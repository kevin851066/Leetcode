import math

class Solution:
    def checkPerfectNumber(self, num):
        '''
        type: num: int
        rtype: bool
        '''
        if num == 1:
            return False
        dvs = []
        sqrt = math.sqrt(num)
        for i in range(1, int(sqrt)+1):
            if num % i == 0:
                dvs.append(i)
                dvs.append(num//i)
        
        return sum(dvs) == num * 2

        
    