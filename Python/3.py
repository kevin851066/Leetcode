class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0 # sliding window
        max_length = 0
        used_char = set() # like dictionary, but without value
        while right < len(s):
            if s[right] not in used_char:
                used_char.add(s[right])
                right += 1
                max_length = max(max_length, right-left) # when right += 1, the max_length may update, but when left += 1, the max_length won't update. 
            else:
                used_char.remove(s[left]) # keep remove char until there is no duplicate char in the sliding window 
                left += 1
        return max_length