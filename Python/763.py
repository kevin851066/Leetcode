class Solution:
    def partitionLabels(self, S):
        '''
        :type: S: str
        :rtype: List[int]
        '''
        itv = {}
        for i, c in enumerate(S):
            if c not in itv:
                itv[c] = [i, 0]
            else:
                itv[c][1] = i
        itvs = list(itv.values())
        
        res = []
        for i in range(len(itvs)-1):
            s1, e1 = itvs[i]
            s2, e2 = itvs[i+1]
            if e1 >= s2:
                itvs[i+1] = [s1, max(e1, e2)]
            else:
                res.append(itvs[i])
        res.append(itvs[-1])
        return [i[1]-i[0]+1 if i[1] != 0 else 1 for i in res]
            
            