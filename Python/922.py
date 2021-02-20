class Solution:
    def sortArrayByParityII(self, A):
        '''
        :type: A: List[int]
        :rtype: List[int]
        '''
        even_idx, odd_idx = 0, 1
        while even_idx < len(A) and odd_idx < len(A):
            if A[even_idx] % 2 == 0:
                even_idx += 2
            else:
                A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
                odd_idx += 2
        return A