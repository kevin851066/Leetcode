class Solution:
    def threeSum(self, nums):
        '''
        :type: nums: List[int]
        :rtype: List[List[int]]
        '''
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i+1, len(nums) - 1  
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        output.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < 0:
                        l += 1
                    else:
                        r -= 1
        return output
            
        