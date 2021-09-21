class Solution:
    def subsetsWithDup(self, nums):
        '''
        :type: 
            - nums: List[int]
        :rtype: List[List[int]]
        '''
        res = []
        nums = sorted(nums)
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # avoid duplicate
                continue
            self.dfs(nums[i+1:], path + [nums[i]], res)