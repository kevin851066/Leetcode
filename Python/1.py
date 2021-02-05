class Solution:
    def twoSum(self, nums, target):
        """
        :type target: int
              nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [i, d[nums[i]]]
            else:
                d[target - nums[i]] = i