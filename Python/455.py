class Solution:
    def findContentChildren(self, g, s):
        '''
        type: g: List[int]
        type: s: List[int]
        rtype: int
        '''
        s, g = sorted(s), sorted(g)
        idx_g = 0 
        output = 0
        for j in range(len(s)):
            if idx_g < len(g) and g[idx_g] <= s[j]:
                idx_g += 1
                output += 1
        return output      