class Solution:
    '''
    :type: s: str
    :rtype: int
    '''
    def romanToInt_1(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        output, prev = 0, 0
        for i in s[::-1]:
            if d[i] >= prev:
                output += d[i]               
            else:
                output -= d[i]
            prev = d[i]
        return output
    
    def romanToInt_2(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return d[s]
        else:
            output = 0            
            for i in range(1, len(s)):
                if d[s[i]] > d[s[i-1]]:
                    output -= d[s[i-1]]                
                else:
                    output += d[s[i-1]]
            output += d[s[i]]
            return output