class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        :type: n: int
        :rtype: List[str]
        '''
        res = []
        self.dfs(n, 1, 0, '(', res)
        return res
        
    def dfs(self, n, l_num, r_num, path, res):
        if l_num == n:
            if r_num == n:
                res.append(path)
                return
            else:
                self.dfs(n, l_num, r_num+1, path+')', res)
        else: # if l_num < n:
            self.dfs(n, l_num+1, r_num, path+'(', res)
            if l_num > r_num:
                self.dfs(n, l_num, r_num+1, path+')', res)