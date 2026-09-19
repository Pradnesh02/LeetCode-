from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def get_digit_sum(num: int) -> int:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        # Count frequencies of each digit sum
        sum_counts = Counter(get_digit_sum(i) for i in range(1, n + 1))
        
        # Find the maximum size among the groups
        max_size = max(sum_counts.values())
        
        # Count how many groups achieve this maximum size
        return sum(1 for count in sum_counts.values() if count == max_size)