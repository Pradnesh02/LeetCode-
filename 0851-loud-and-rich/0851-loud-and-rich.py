from collections import defaultdict


class Solution:

  def loudAndRich(
      self, richer: list[list[int]], quiet: list[int]
  ) -> list[int]:
    n = len(quiet)
    graph = defaultdict(list)

    # Build directed graph from poorer to richer (v -> u where u is richer than v)
    for u, v in richer:
      graph[v].append(u)

    # ans[i] stores the person who is richest >= i with the minimum quiet value
    ans = [-1] * n

    def dfs(node: int) -> int:
      if ans[node] != -1:
        return ans[node]

      # Start by assuming the person themselves is the quietest
      least_quiet_person = node

      # Check all people who are richer than this person
      for richer_person in graph[node]:
        candidate = dfs(richer_person)
        if quiet[candidate] < quiet[least_quiet_person]:
          least_quiet_person = candidate

      ans[node] = least_quiet_person
      return least_quiet_person

    for i in range(n):
      dfs(i)

    return ans