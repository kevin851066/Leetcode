class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        '''
        :type: nums: List[int]
        :type: k: int
        :rtype: bool
        '''
        s = sum(nums)
        l = len(nums)
        if s % k != 0:
            return False
        subsum = s // k
        subset = [0] * k
        nums.sort(reverse=True)
        
        def solver(i):
            if i == l:
                return len(set(subset)) == 1    # check all subset are eqaul
            for j in range(k):
                subset[j] += nums[i]
                if subset[j] <= subsum and solver(i + 1):
                    return True
                subset[j] -= nums[i]
                if subset[j] == 0:
                    break
            return False

        return solver(0)
