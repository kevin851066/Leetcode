class Solution:
    def countGoodRectangles(self, rectangles):
        '''
        :type: rectangles: List[List[int]]
        :rtype: int
        '''
        maxLen = -float('inf')
        res = 1
        for rec in rectangles:
            if maxLen < min(rec):
                maxLen = min(rec)
                res = 1
            elif maxLen == min(rec):
                res += 1
        
        return res