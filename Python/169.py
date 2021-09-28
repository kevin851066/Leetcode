class Solution:
    def majorityElement(self, nums):
        '''
        :type: nums: List[int]
        :rtype: int
        '''
        nums = sorted(nums)
        return nums[len(nums)//2]

# Boyer-Moore Voting Algorithm
class Solution2:
    def majorityElement(self, nums):
        '''
        :type: nums: List[int]
        :rtype: int
        '''
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            if num == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate