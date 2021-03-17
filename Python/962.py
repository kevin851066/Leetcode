class Solution:
    def maxWidthRamp(self, A):
        '''
        :type: A: List[int]
        :rtype: int
        '''
        stk = []
        ji = 0
        for i, a in enumerate(A):
            if not stk or A[stk[-1]] > a:
                stk.append(i)
        for j in range(len(A)-1,-1,-1):
            while stk and A[j] >= A[stk[-1]]:
                ji = max(ji, j - stk.pop())
        return ji