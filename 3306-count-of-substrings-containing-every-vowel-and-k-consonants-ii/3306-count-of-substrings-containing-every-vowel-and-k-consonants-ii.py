from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        
        def atLeast(c: int) -> int:
            vowel_counts = defaultdict(int)
            consonants = 0
            left = 0
            ans = 0
            n = len(word)
            
            for right in range(n):
                ch = word[right]
                if ch in vowels:
                    vowel_counts[ch] += 1
                else:
                    consonants += 1
                    
                while len(vowel_counts) == 5 and consonants >= c:
                    ans += (n - right)
                    
                    left_ch = word[left]
                    if left_ch in vowels:
                        vowel_counts[left_ch] -= 1
                        if vowel_counts[left_ch] == 0:
                            del vowel_counts[left_ch]
                    else:
                        consonants -= 1
                    left += 1
                    
            return ans
            
        return atLeast(k) - atLeast(k + 1)