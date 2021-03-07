class Solution:
    def combinationSum2(self, candidates, target):
        '''
        :type: candidates: List[int]
        :type: target: int
        :rtype: List[List[int]]
        '''
        res = []
        candidates.sort()
        self.solver([], candidates, 0, target, res)
        return res
        
    def solver(self, nums, candidates, idx, remain, res):
        if remain == 0:
            res.append(nums)
        else:
            for i in range(idx, len(candidates)):
                if i == idx or candidates[i] != candidates[i-1]:
                    if remain - candidates[i] < 0:
                        break
                    else:
                        self.solver(nums + [candidates[i]], candidates, i+1, remain - candidates[i], res)
                    