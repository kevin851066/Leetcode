from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        type: s: str
        :rtype: List[str]
        '''
        d = defaultdict(int)
        cnt = 0 
        for i in range(len(s)):
            d[s[i]] += 1
            
        for k, v in d.items():
            if v % 2 == 1:
                cnt += 1
        return len(s) if cnt <= 1 else len(s) - cnt + 1