class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        def get_next_jumps(indices: list[int]) -> list[int]:
            next_jump = [-1] * n
            stack = []
            for i in indices:
                while stack and stack[-1] < i:
                    next_jump[stack.pop()] = i
                stack.append(i)
            return next_jump

        # Sort indices to find the smallest greater/equal or largest smaller/equal elements
        # For odd jump: smallest arr[j] >= arr[i] with minimal j
        sorted_by_val_asc = sorted(range(n), key=lambda i: arr[i])
        next_odd = get_next_jumps(sorted_by_val_asc)

        # For even jump: largest arr[j] <= arr[i] with minimal j
        sorted_by_val_desc = sorted(range(n), key=lambda i: -arr[i])
        next_even = get_next_jumps(sorted_by_val_desc)

        # odd[i]: can we reach the end from index i making an odd jump?
        # even[i]: can we reach the end from index i making an even jump?
        odd = [False] * n
        even = [False] * n

        # Base case: the last index is always valid
        odd[-1] = True
        even[-1] = True

        # Traverse backwards and determine reachability using dynamic programming
        for i in range(n - 2, -1, -1):
            if next_odd[i] != -1:
                odd[i] = even[next_odd[i]]
            if next_even[i] != -1:
                even[i] = odd[next_even[i]]

        return sum(odd)