class Solution:
    def letterCombinations(self, digits: str) -> List[str]:  
        '''
        :type: digits: str
        :rtype: List[str]
        '''
        if len(digits) == 0:
            return []
        _dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        thres = len(digits)
        res = []
        self.dfs(_dict, digits, 0, thres, '', res)
        return res
    
    def dfs(self, _dict, digits, level, thres, substr, res):
            if level == thres:
                res.append(substr)
                return 
            for char in _dict[digits[level]]:
                self.dfs(_dict, digits, level+1, thres, substr + char, res)