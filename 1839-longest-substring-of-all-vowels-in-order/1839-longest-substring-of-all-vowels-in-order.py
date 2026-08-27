class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word) < 5:
            return 0
            
        max_len = 0
        curr_len = 1
        unique_vowels = 1
        
        for i in range(1, len(word)):
            if word[i] >= word[i - 1]:
                curr_len += 1
                if word[i] > word[i - 1]:
                    unique_vowels += 1
            else:
                curr_len = 1
                unique_vowels = 1
                
            if unique_vowels == 5:
                max_len = max(max_len, curr_len)
                
        return max_len