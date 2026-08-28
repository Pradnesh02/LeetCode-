from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = {}
        # Stores list of tuples: (rule_index, pattern_str)
        self.patterns = []


class Solution:

    def minCost(
        self,
        source: str,
        target: str,
        rules: list[list[str]],
        costs: list[int],
    ) -> int:
        n = len(source)

        # Precompute effective cost of each rule: base_cost + number of '*'
        effective_costs = []
        # Group rules by replacement string in a Trie for efficient matching against target
        root = TrieNode()

        for idx, (pattern, replacement) in enumerate(rules):
            star_count = pattern.count("*")
            effective_costs.append(costs[idx] + star_count)

            curr = root
            for ch in replacement:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]

            curr.patterns.append((idx, pattern))

        # dp[i] represents the minimum cost to convert source[:i] to target[:i]
        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            # Option 1: Characters already match, 0 cost to skip/keep character
            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]

            # Option 2: Match replacement against target starting at index i using Trie
            curr = root
            for j in range(i, n):
                ch = target[j]
                if ch not in curr.children:
                    break
                curr = curr.children[ch]

                # Check all rules ending at index j
                for rule_idx, pattern in curr.patterns:
                    length = len(pattern)
                    # Verify if pattern matches source[i : j + 1]
                    matches = True
                    for k in range(length):
                        if (
                            pattern[k] != "*"
                            and pattern[k] != source[i + k]
                        ):
                            matches = False
                            break

                    if matches:
                        total_cost = dp[i] + effective_costs[rule_idx]
                        if total_cost < dp[j + 1]:
                            dp[j + 1] = total_cost

        return dp[n] if dp[n] != INF else -1