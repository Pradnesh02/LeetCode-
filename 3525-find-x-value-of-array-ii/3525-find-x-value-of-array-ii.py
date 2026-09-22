from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_count = [[0] * self.k for _ in range(4 * self.n)]
        self.nums = nums
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _merge(self, p1: int, c1: List[int], p2: int, c2: List[int]):
        new_p = (p1 * p2) % self.k
        new_c = list(c1)
        for r, cnt in enumerate(c2):
            if cnt:
                rem = (p1 * r) % self.k
                new_c[rem] += cnt
        return new_p, new_c

    def _build(self, node: int, l: int, r: int):
        if l == r:
            val_mod = self.nums[l] % self.k
            self.tree_prod[node] = val_mod
            self.tree_count[node][val_mod] = 1
            return
        
        mid = (l + r) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        self._build(left_child, l, mid)
        self._build(right_child, mid + 1, r)
        
        self.tree_prod[node], self.tree_count[node] = self._merge(
            self.tree_prod[left_child], self.tree_count[left_child],
            self.tree_prod[right_child], self.tree_count[right_child]
        )

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            val_mod = val % self.k
            self.tree_prod[node] = val_mod
            self.tree_count[node] = [0] * self.k
            self.tree_count[node][val_mod] = 1
            return
        
        mid = (l + r) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        if idx <= mid:
            self.update(left_child, l, mid, idx, val)
        else:
            self.update(right_child, mid + 1, r, idx, val)
            
        self.tree_prod[node], self.tree_count[node] = self._merge(
            self.tree_prod[left_child], self.tree_count[left_child],
            self.tree_prod[right_child], self.tree_count[right_child]
        )

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_count[node]
        
        mid = (l + r) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        
        if qr <= mid:
            return self.query(left_child, l, mid, ql, qr)
        if ql > mid:
            return self.query(right_child, mid + 1, r, ql, qr)
        
        p1, c1 = self.query(left_child, l, mid, ql, qr)
        p2, c2 = self.query(right_child, mid + 1, r, ql, qr)
        return self._merge(p1, c1, p2, c2)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = SegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            # 1. Update nums[idx] = val persistently
            seg_tree.update(1, 0, n - 1, idx, val)
            
            # 2. Query prefix product remainder counts on subarray nums[start...n-1]
            _, count = seg_tree.query(1, 0, n - 1, start, n - 1)
            ans.append(count[x])
            
        return ans