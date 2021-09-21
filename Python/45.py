class Solution:
    def jump(self, nums):
        '''
        :type: nums: List[int]
        :rtype: int
        '''
        if len(nums) == 1:
            return 0
        l, r = 0, nums[0]
        steps = 1
        while r < len(nums) - 1:
            r_nxt = max([nums[i] + i for i in range(l, r+1)])
            l, r = r+1, r_nxt
            steps += 1
        return steps
            