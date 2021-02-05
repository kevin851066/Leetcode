class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]x
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        org_r = len(nums)
        org_c = len(nums[0])
        
        if r*c != org_r * org_c:
            return nums
        else:
            tmp, output = [], []
            for num in nums:
                tmp += num
            for i in range(r):
                output.append(tmp[i*c: (i+1)*c])
            return output
                