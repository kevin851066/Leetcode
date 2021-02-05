class Solution:
    def removeElement(self, nums, val):
        '''
        type: nums: List[int]
        type: val: int
        rtype: int
        '''
        real = 0
        for i in range(len(nums)):
            if nums[i] != val:  
                nums[real] = nums[i]
                real += 1
        return real