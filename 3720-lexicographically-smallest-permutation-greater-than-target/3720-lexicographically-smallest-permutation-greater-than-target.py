from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_count = Counter(s)
        prefix_count = Counter()
        
        # Precompute prefix counts of target to quickly check availability
        valid_prefix_len = 0
        for i in range(n):
            if prefix_count[target[i]] + 1 <= total_count[target[i]]:
                prefix_count[target[i]] += 1
                valid_prefix_len += 1
            else:
                break
                
        # Try finding the divergence point from right to left
        for i in range(valid_prefix_len, -1, -1):
            # Calculate remaining characters after matching target[:i]
            remaining = total_count.copy()
            for j in range(i):
                remaining[target[j]] -= 1
            
            if i < n:
                # Find the smallest available character strictly greater than target[i]
                for code in range(ord(target[i]) + 1, ord('z') + 1):
                    ch = chr(code)
                    if remaining[ch] > 0:
                        remaining[ch] -= 1
                        
                        # Construct the smallest suffix
                        suffix = []
                        for c_code in range(ord('a'), ord('z') + 1):
                            c = chr(c_code)
                            if remaining[c] > 0:
                                suffix.append(c * remaining[c])
                                
                        return target[:i] + ch + "".join(suffix)
                        
        return ""