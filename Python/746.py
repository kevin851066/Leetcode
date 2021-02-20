class Solution:
    def minCostClimbingStairs(self, cost):
        '''
        :type: cost: List[int]
        :rtype: int
        '''
        min_cost = [cost[0], cost[1]] # min_cost = [cost[0], min(cost[1], cost[0]+cost[1])]
        for c in range(2, len(cost)):
            min_cost.append(min(min_cost[c-2], min_cost[c-1]) + cost[c]) # min_cost.append(min(min_cost[c-2]+cost[c], min_cost[c-1]+cost[c]))
        return min(min_cost[-1], min_cost[-2])