class Solution:
    def searchInsert(self, nums, target):
        '''
        :type: nums: List[int]
        :type: target: int
        :rtype: int
        '''
        low, high, mid = 0, len(nums)-1, 0
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low  # since when we don't find the target, the low index will be the index of the element just greater than target, that is the place we want.