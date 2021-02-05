class Solution:
    def findAnagrams(self, s, p):
        '''
        type: s: str
        type: p: str
        rtype: List[int]
        '''
        l = len(p)
        ds, dp = {}, {}
        output = []
        
        for i in p:
            dp[i] = dp[i] + 1 if i in dp else 1
        
        sfirst = ''
        for j in range(len(s)-l+1):
            sfirst = s[j]
            if j == 0:
                for k in s[j:j+l]:
                    ds[k] = ds[k] + 1 if k in ds else 1
            else:
                ds[s[j+l-1]] = ds[s[j+l-1]] + 1 if s[j+l-1] in ds else 1
            if dp == ds:
                output.append(j)
            ds[sfirst] -= 1
            if ds[sfirst] == 0:
                del ds[sfirst]
                
        return output