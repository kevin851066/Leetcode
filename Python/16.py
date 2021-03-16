class Solution:
    def threeSumClosest(self, nums, target):
        '''
        :type: nums: List[int]
        :type: target: int
        :rtype: int
        '''
        nums.sort()
        dis = float('inf')
        res = 0
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                l, r = i + 1, len(nums) - 1
                while r > l:
                    s = nums[i] + nums[r] + nums[l]
                    diff = abs(target - s)
                    if diff < dis:
                        dis = diff
                        res = s
                    if target > s:
                        while r > l and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                    elif target < s:
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                    else:
                        return res
        return res
                        