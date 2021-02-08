class Solution:
    def permute(self, nums):
        '''
        type: nums: List[int]
        rtype: List[List[int]]
        '''
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)