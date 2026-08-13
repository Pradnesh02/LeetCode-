class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            # Add character at right pointer to frequency count
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Update the frequency of the most frequent character in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Window length is (right - left + 1)
            # If (window length - max_freq) > k, the window is invalid
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len