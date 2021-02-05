class Solution:
    def containsNearbyDuplicate(self, nums, k):
        '''
        type: nums: List[int]
        type: k: int
        rtype: bool
        '''
        d = {}
        for i, j in enumerate(nums):
            if j in d and i - d[j] <= k:
                return True  
            d[j] = i
        return False