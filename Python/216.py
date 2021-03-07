class Solution:
    def combinationSum3(self, k, n):
        '''
        :type: k: int
        :type: n: int
        :rtype: List[List[int]]
        '''
        res = []
        self.solver(n, k, 1, [], res)
        return res
    
    def solver(self, remand, k, idx, nums, res):
        if k >= 0:
            if remand == 0 and k == 0:
                res.append(nums)
            else:
                for i in range(idx, 10):
                    if remand - i < 0:
                        break
                    else:
                        self.solver(remand - i, k - 1, i + 1, nums + [i], res)