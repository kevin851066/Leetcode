class Solution:
    def isPalindrome(self, x):
        '''
        :type: x: int
        :rtype: bool
        '''
        s = str(x)
        l = len(s)
        if '-' == s[0]:
            return False
        for i in range(l//2):
            if s[i] != s[-(i+1)]:
                return False
        return True
    
    def isPalindrome2(self, x):
        '''
        :type: x: int
        :rtype: bool
        '''
        s = str(x)
        if '-' == s[0]:
            return False
        return s == s[::-1]