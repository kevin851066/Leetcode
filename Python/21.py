class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest, profit = float('inf'), 0
        for i in prices:
            if i < lowest:
                lowest = i
            elif profit < i - lowest:
                profit = i - lowest
        return profit