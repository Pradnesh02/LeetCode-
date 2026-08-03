import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        
        # Step 1: Count frequency of each number in nums
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            
        # Step 2: Count how many numbers in nums are multiples of g
        multiples = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for m in range(g, max_val + 1, g):
                multiples[g] += freq[m]
                
        # Step 3: Compute exact count of pairs whose GCD is equal to g
        # exact_gcd[g] = total pairs with common divisor g - sum(exact_gcd[k*g] for k >= 2)
        exact_gcd = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            c = multiples[g]
            # Total pairs whose numbers are both multiples of g
            total_pairs = c * (c - 1) // 2
            
            # Subtract pairs whose GCD is a strict multiple of g
            sub = 0
            for m in range(2 * g, max_val + 1, g):
                sub += exact_gcd[m]
                
            exact_gcd[g] = total_pairs - sub

        # Step 4: Build prefix sums of GCD frequencies (from gcd = 1 to max_val)
        prefix_sum = []
        gcd_values = []
        running_sum = 0
        
        for g in range(1, max_val + 1):
            if exact_gcd[g] > 0:
                running_sum += exact_gcd[g]
                prefix_sum.append(running_sum)
                gcd_values.append(g)

        # Step 5: Answer each query using binary search (bisect_right)
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sum, q)
            ans.append(gcd_values[idx])

        return ans