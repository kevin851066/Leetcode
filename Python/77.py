class Solution:
    def combine(self, n, k):
        '''
        :type: n: int
        :type: k: int
        :rtype: List[List[int]]
        '''
        res = []
        self.solver(1, n, k, [], res)
        return res
        
    def solver(self, start_num, n, k, nums, res):
        if nums == [n]:
            print(nums)
            return
        if len(nums) == k:
            res.append(nums)
        else:
            for i in range(start_num, n+1):
                nums = nums + [i]
                self.solver(i+1, n, k, nums, res)
            
            
            