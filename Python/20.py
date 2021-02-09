class Solution:
    def isValid(self, s):
        '''
        type: s: str
        rtype: bool
        '''
        if len(s) % 2 == 1:
            return False
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in d:   # '(', '{', '['
                stack.append(char)
            else:           # ')', '}', ']'
                if len(stack) == 0:
                    return False
                elif char != d[stack.pop()]:
                    return False
        return len(stack) == 0