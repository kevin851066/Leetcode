class Solution:
    def lemonadeChange(self, bills):
        '''
        type: bills: List[int]
        rtype: bool
        '''
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1 
            elif i == 10:
                five -= 1
                ten += 1 
            elif ten > 0:  # i = 20, give 10 first
                ten -= 1
                five -= 1
            else:         # i = 20, if no 10 in handy, give 5 
                five -= 3
            if five < 0:
                return False
        return True