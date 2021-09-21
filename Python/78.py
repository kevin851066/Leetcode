class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        :nums: List[int]
        :rtype: List[List[int]]
        '''
        res = []
        length = len(nums)
        self.solver(length, nums, [], res)
        return res
        
    def solver(self, length, nums, path, res):
        if length == 0:
            res.append(path)
            return
        self.solver(length - 1, nums[1:], path + [nums[0]], res)
        self.solver(length - 1, nums[1:], path, res)         