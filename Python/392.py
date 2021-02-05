class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        type: s: str
        type: t: str
        rtype: bool
        '''
        idx = 0
        for char in t:
            if idx == len(s): # avoid empty s
                break
            if char == s[idx]:
                idx += 1
        return idx == len(s)