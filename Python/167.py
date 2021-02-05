class Solution:
    def TwoPointers(self, numbers, target):
        """
        :type numbers: List[int],
              target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l+1, r+1]

    def BinarySearch(self, numbers, target):
        """
        :type numbers: List[int],
              target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            while l <= r: # l and r may converge to the same value
                mid = (l+r) // 2
                if numbers[mid] > target-numbers[i]:
                    r = mid-1
                elif numbers[mid] < target-numbers[i]:
                    l = mid+1
                else:
                    return [i+1, mid+1]