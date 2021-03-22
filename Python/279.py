class Solution:
    def numSquares(self, n):
        '''
        :type: n: int
        :rtype: int
        '''
        i = 1
        sqlist = []
        while i**2 <= n:
            sqlist.append(i**2)
            i += 1
        cnt = 0
        remain_list = {n}        
        while remain_list:
            cnt += 1
            tmp = set()
            for r in remain_list:
                for sq in sqlist:
                    if r == sq:
                        return cnt
                    elif r < sq:
                        break
                    else:
                        tmp.add(r-sq)
            remain_list = tmp
            