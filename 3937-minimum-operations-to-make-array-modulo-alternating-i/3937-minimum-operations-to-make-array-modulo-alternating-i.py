class Solution:

    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Count occurrences of each remainder at even and odd indices
        count_even = [0] * k
        count_odd = [0] * k

        for i in range(n):
            rem = nums[i] % k
            if i % 2 == 0:
                count_even[rem] += 1
            else:
                count_odd[rem] += 1

        # Distance function between remainder r and target remainder t
        def dist(r: int, t: int) -> int:
            diff = (t - r) % k
            return min(diff, k - diff)

        # Calculate total cost to change all even/odd indices to remainder x/y
        cost_even = [0] * k
        cost_odd = [0] * k

        for target in range(k):
            for r in range(k):
                if count_even[r]:
                    cost_even[target] += count_even[r] * dist(r, target)
                if count_odd[r]:
                    cost_odd[target] += count_odd[r] * dist(r, target)

        # Find the best and second-best remainders for even and odd positions
        even_sorted = sorted(range(k), key=lambda x: cost_even[x])
        odd_sorted = sorted(range(k), key=lambda y: cost_odd[y])

        # Pick distinct x and y that minimize the total cost
        ans = float("inf")
        for x in even_sorted[:2]:
            for y in odd_sorted[:2]:
                if x != y:
                    ans = min(ans, cost_even[x] + cost_odd[y])

        return ans