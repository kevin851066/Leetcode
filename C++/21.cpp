class Solution {
public:
    int maxProfit(vector<int>& prices) {
        """
        :type: prices: vector<int>
        :rtype: int
        """
        int lowest = INT_MAX, profit = 0;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < lowest)
                lowest = prices[i];
            else if (profit < prices[i] - lowest) 
                profit = prices[i] - lowest;
        }
        return profit;
    }
};