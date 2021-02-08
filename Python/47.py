class Solution:
    def permuteUnique(self, nums):
        '''
        type: nums: List[int]
        rtype: List[List[int]]
        '''
        res = []
        nums = sorted(nums)
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
        else:
            for i in range(len(nums)):
                if i == 0:
                    self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
                elif nums[i] != nums[i-1]:
                    self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)