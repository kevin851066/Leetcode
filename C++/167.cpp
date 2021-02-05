class Solution {
public:
    vector<int> TwoPointers(vector<int>& numbers, int target) {
        """
        :type: nums: vector<int>
        :type: target: int
        :rtype: array
        """
        int l = 0, r = numbers.size()-1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s > target) 
                r -= 1;
            else if (s < target)
                l += 1;
            else
                return {l+1, r+1};
        }
        return {};
    }

    vector<int> BinarySearch(vector<int>& numbers, int target) {
        """
        :type: nums: vector<int>
        :type: target: int
        :rtype: array
        """
        for (int i = 0; i < numbers.size(); i++) {
            int l = i+1, r = numbers.size()-1;
            while (l <= r) {
                int mid = (l+r) / 2;
                if (numbers[mid] > target - numbers[i])
                    r = mid - 1;
                else if (numbers[mid] < target - numbers[i])
                    l = mid + 1;
                else
                    return {i+1, mid+1};
            }
        }
        return {};
    }
};
};