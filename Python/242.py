class Solution:
    def isAnagram(self, s, t):
        '''
        type: s: str
        type: t: str
        rtype: bool
        '''
        d1, d2 = {}, {}
        for i in s:
            d1[i] = 1 if i not in d1 else d1[i] + 1
        for j in t:
            d2[j] = 1 if j not in d2 else d2[j] + 1
                
        return d1 == d2