class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        """
        :type: nums: vector<int>
        :type: target: int
        :rtype: array
        """
        unordered_map<int, int> d;
        for (int i = 0; i < nums.size(); i++) {
            if (d.count(nums[i]) == 1)
                return {d[nums[i]], i};
            else
                d[target-nums[i]] = i;
        }
        return {};
    }
};