class Solution {
public:
    int maxProfit(vector<int>& prices) {
        '''
        :type: prices: vector<int>
        rtype: int
        '''
        int profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1]) 
                profit += (prices[i] - prices[i-1]);
        }
        return profit;
    }
};