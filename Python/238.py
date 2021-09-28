class Solution:
    def productExceptSelf(self, nums):
        '''
        :type: nums: List[int]
        :rtype: List[int]
        '''
        tmp1 = 1
        mem = [1] * len(nums)
        for idx in range(len(nums)):
            mem[idx] *= tmp1
            tmp1 *= nums[idx]
        tmp1 = 1
        for idx in range(len(nums) - 1, -1, -1):
            mem[idx] *= tmp1
            tmp1 *= nums[idx]
        return mem