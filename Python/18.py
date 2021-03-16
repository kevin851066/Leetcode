class Solution:
    def fourSum(self, nums, target):
        '''
        :type: nums: List[int]
        :type: target: int
        :rtype: List[List[int]]
        '''
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if nums[i] > target/4:
                break
            target1 = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, len(nums)-2):
                    if nums[j] > (target1) / 3:
                        break
                    target2 = target1 - nums[j]
                    if j == i+1 or nums[j] != nums[j-1]:
                        l, r = j + 1, len(nums) - 1
                        while l < r:
                            s = target2 - nums[l] - nums[r]
                            if s == 0:
                                res.append([nums[i], nums[j], nums[l], nums[r]])
                                while l < r and nums[l] == nums[l+1]:
                                    l += 1
                                while l < r and nums[r] == nums[r-1]:
                                    r -= 1
                                l += 1
                                r -= 1
                            elif s > 0:
                                while l < r and nums[l] == nums[l+1]:
                                    l += 1
                                l += 1
                            else:
                                while l < r and nums[r] == nums[r-1]:
                                    r -= 1
                                r -= 1
        return res