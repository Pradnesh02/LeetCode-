from collections import Counter, defaultdict

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        required = len(target_counts)
        
        window_counts = defaultdict(int)
        formed = 0
        
        left = 0
        min_len = float('inf')
        best_window = (0, 0)
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1
            
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
                
            # Try contracting the window from the left
            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    best_window = (left, right)
                    
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                    
                left += 1
                
        return "" if min_len == float('inf') else s[best_window[0]:best_window[1] + 1]