class Solution:
    def combinationSum(self, candidates, target):
        '''
        :type: candidates: List[int]
        :type: target: int
        :rtype: List[List[int]]
        '''
        res = []
        candidates.sort()
        self.solver(candidates, [], 0, target, res)
        return res
        
    def solver(self, candidates, nums, total, target, res):
        if total == target:
            res.append(nums)
        else: 
            for i in range(len(candidates)):
                if total + candidates[i] > target:
                    break
                else:
                    self.solver(candidates[i:], nums + [candidates[i]], total + candidates[i], target, res)
                    