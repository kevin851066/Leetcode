class Solution:
    def canJump(self, nums):
        '''
        :type: nums: List[int]
        :rtype: bool
        '''
        max_dis = [-1] * len(nums)
        max_dis[0] = 1
        for idx, max_jump_length in enumerate(nums):
            if max_dis[idx] == 1:
                if idx + max_jump_length > len(nums) - 1:
                    upperbound = len(nums) - 1
                else:
                    upperbound = idx + max_jump_length
                for i in range(idx+1, upperbound+1):
                    max_dis[i] = 1
                if max_dis[-1] == 1:
                    return True
                # print(idx, max_dis)
        return max_dis[-1] == 1

class Solution:
    def canJump(self, nums):
        '''
        :type: nums: List[int]
        :rtype: bool
        '''
        last_position = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0

class Solution:
    def canJump(self, nums):
        '''
        :type: nums: List[int]
        :rtype: bool
        '''
        mem = [0] * len(nums)
        mem[0] = nums[0]
        for i in range(1, len(nums)):
            if mem[i-1] < i: # idx i can't be reached
                return False
            mem[i] = max(mem[i-1], nums[i]+i)
            if mem[i] >= len(nums) - 1:
                return True
        return True # execute to the end and no False return, return True
