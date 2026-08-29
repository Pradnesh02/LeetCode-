from collections import defaultdict
from typing import List


class Solution:

  def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    parent = list(range(n))

    def find(x: int) -> int:
      if parent[x] != x:
        parent[x] = find(parent[x])
      return parent[x]

    def union(x: int, y: int) -> None:
      root_x, root_y = find(x), find(y)
      if root_x != root_y:
        parent[root_x] = root_y

    # Group connected indices using Disjoint Set Union (DSU)
    for u, v in pairs:
      union(u, v)

    # Collect characters and indices belonging to the same connected component
    groups = defaultdict(list)
    for i in range(n):
      groups[find(i)].append(i)

    # Place sorted characters back into their respective sorted positions
    res = list(s)
    for indices in groups.values():
      chars = sorted([s[i] for i in indices])
      for idx, ch in zip(sorted(indices), chars):
        res[idx] = ch

    return "".join(res)