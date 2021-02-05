class Solution:
    def removeDuplicates(self, nums):
        '''
        : type: nums: List[int]
        : rtype: int
        '''
        real = 0    # output tail idx
        for i in range(len(nums)-1):
            tmp = nums[i]
            if tmp != nums[i+1]:    # no duplicate
                real += 1
                nums[real] = nums[i+1]
        return real+1