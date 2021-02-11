class Solution:
    def totalHammingDistance(self, nums):
        '''
        :type: nums: List[int]
        :rtype: int
        '''
        code = []
        for i in range(len(nums)):
            code.append('{:032b}'.format(nums[i]))
        output = 0
        for i in range(32):
            s = ''
            for j in range(len(code)):
                s += code[j][i]
            output += s.count('0') * s.count('1')
        return output