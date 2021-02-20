class Solution:
    def sortArrayByParity_sol1(self, A):
        '''
        :type: A: List[int]
        :rtype: List[int]
        '''
        even_arr, odd_arr = [], []
        for i in A:
            if i % 2 == 0:
                even_arr.append(i)
            else:
                odd_arr.append(i)
        return even_arr + odd_arr
        
    def sortArrayByParity_sol2(self, A):
        '''
        :type: A: List[int]
        :rtype: List[int]
        '''
        l, r = 0, len(A)-1
        while r >= l:
            if A[l] % 2 == 0:
                l += 1
            else:
                A[l], A[r] = A[r], A[l]
                r -= 1
        return A