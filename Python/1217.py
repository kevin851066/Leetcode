class Solution:
    def minCostToMoveChips(self, position):
        '''
        :type: position: List[int]
        :rtype: int
        '''
        even_cost, odd_cost = 0, 0
        for pos in position:
            if pos % 2 == 1:
                odd_cost += 1 # cost for moving all odd to even
            else:
                even_cost += 1 # cost for moving all even to odd
        return min(even_cost, odd_cost)