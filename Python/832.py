class Solution:
    def flipAndInvertImage(self, A):
        '''
        type: A: List[List[int]]
        rtype: List[List[int]]
        '''
        B = []
        for a in A:
            b = a[::-1]
            for i in range(len(b)):
                b[i] = b[i] ^ 1 
            B.append(b)
        return B