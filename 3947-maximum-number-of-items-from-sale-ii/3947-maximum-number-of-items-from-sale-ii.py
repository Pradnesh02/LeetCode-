from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # 1. Frequency of each factor and global minimum price
        freq = [0] * (n + 1)
        min_price = float('inf')
        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)
            
        # 2. Compute count of multiples for each factor in O(n log n)
        multiples = [0] * (n + 1)
        for i in range(1, n + 1):
            if freq[i] > 0:
                for j in range(i, n + 1, i):
                    multiples[i] += freq[j]
                    
        # 3. Create pairs of (price, k_i) where k_i is available bonus capacity
        bonus_items = []
        for factor, price in items:
            k_i = multiples[factor] - 1
            if k_i > 0 and price < 2 * min_price:
                bonus_items.append((price, k_i))
                
        # 4. Sort bonus-eligible items by price ascending
        bonus_items.sort(key=lambda x: x[0])
        
        # 5. Greedy purchase
        ans = budget // min_price
        cur_items = 0
        rem_budget = budget
        
        for price, k_i in bonus_items:
            take = min(k_i, rem_budget // price)
            rem_budget -= take * price
            cur_items += take * 2
            
            ans = max(ans, cur_items + (rem_budget // min_price))
            
            # If we couldn't take all k_i copies, budget is exhausted for further purchases
            if take < k_i:
                break
                
        return ans