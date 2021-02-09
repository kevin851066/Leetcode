class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        type: nums: List[int]
        rtype: none
        '''
        sufidx = len(nums) - 1
        while sufidx > 0 and nums[sufidx-1] - nums[sufidx] >= 0:
            sufidx -= 1
        
        if sufidx - 1 >= 0:
            pivot, j = sufidx - 1, len(nums) - 1
            while j >= sufidx and nums[pivot] >= nums[j]:
                j -= 1
            
            nums[j], nums[pivot] = nums[pivot], nums[j]
            l, r = sufidx, len(nums) - 1
            
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:  
            nums.reverse()
