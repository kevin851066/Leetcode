class Solution:
    def makesquare(self, nums):
        '''
        :type: nums: List[int]
        :rtype: bool
        '''
        s, l = sum(nums), len(nums)
        if l == 0 or s % 4 != 0:
            return False
        buck = [0] * 4
        subsum = s // 4
        nums.sort(reverse=True)
        
        def solver(i):
            if i == l:
                return len(set(buck)) == 1
            for j in range(4):
                buck[j] += nums[i]
                if buck[j] <= subsum and solver(i + 1):
                    return True
                buck[j] -= nums[i]
                if buck[j] == 0:
                    break
            return False
        
        return solver(0)