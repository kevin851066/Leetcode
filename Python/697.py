class Solution:
    def findShortestSubArray(self, nums):
        '''
        :type: nums: List[int]
        :rtype: int
        '''
        itv = {}
        for i, num in enumerate(nums):
            if num not in itv:
                itv[num] = [i, 0, 1]
            else:
                itv[num][1] = i
                itv[num][2] += 1
        m, l = -float('inf'), float('inf')
        
        for i in itv.values():
            if m < i[2]:
                m, l = i[2], i[1] - i[0] + 1
            elif m == i[2]:
                l = min(1, l) if i[1] == 0 else min(l, i[1] - i[0] + 1)
        return l
