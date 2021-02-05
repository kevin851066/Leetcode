class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        """
        :type: s: str
        :rtype: int
        """
       int left = 0, right = 0;
       int max_length = 0;
       set<int> used_char;
       set<int>::iterator iter;
       while (right < s.length()) {
           iter = used_char.find(s[right]);
           if (iter == used_char.end()) {
               used_char.insert(s[right]);
               right += 1;
               max_length = max(max_length, right - left);
           }
           else {
               used_char.erase(s[left]);
               left += 1;
           }
       }
       return max_length;
    }
};