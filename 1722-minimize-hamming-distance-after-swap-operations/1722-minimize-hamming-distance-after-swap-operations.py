from collections import Counter, defaultdict
from typing import List


class Solution:

  def minimumHammingDistance(
      self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
  ) -> int:
    n = len(source)
    parent = list(range(n))

    def find(x: int) -> int:
      if parent[x] != x:
        parent[x] = find(parent[x])
      return parent[x]

    def union(x: int, y: int) -> None:
      root_x, root_y = find(x), find(y)
      if root_x != root_y:
        parent[root_x] = root_y

    # 1. Connect indices that can be swapped
    for u, v in allowedSwaps:
      union(u, v)

    # 2. Group indices by their connected component root
    groups = defaultdict(list)
    for i in range(n):
      groups[find(i)].append(i)

    # 3. For each group, count the elements that cannot be matched between source and target
    hamming_distance = 0
    for indices in groups.values():
      # Count occurrences of elements from source in the current component
      source_counts = Counter(source[i] for i in indices)

      # Check elements required by target in the same component
      for i in indices:
        val = target[i]
        if source_counts[val] > 0:
          source_counts[val] -= 1
        else:
          hamming_distance += 1

    return hamming_distance