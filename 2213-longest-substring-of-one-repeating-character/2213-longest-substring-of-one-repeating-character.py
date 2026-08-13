class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.pref_char = [''] * (4 * self.n)
        self.suff_char = [''] * (4 * self.n)
        
        self._build(s, 1, 0, self.n - 1)

    def _merge(self, node, left, right, left_len, right_len):
        self.pref_char[node] = self.pref_char[left]
        self.suff_char[node] = self.suff_char[right]
        
        self.pref_len[node] = self.pref_len[left]
        self.suff_len[node] = self.suff_len[right]
        
        self.max_len[node] = max(self.max_len[left], self.max_len[right])
        
        if self.suff_char[left] == self.pref_char[right]:
            combined = self.suff_len[left] + self.pref_len[right]
            self.max_len[node] = max(self.max_len[node], combined)
            
            if self.pref_len[left] == left_len:
                self.pref_len[node] = left_len + self.pref_len[right]
                
            if self.suff_len[right] == right_len:
                self.suff_len[node] = right_len + self.suff_len[left]

    def _build(self, s, node, l, r):
        if l == r:
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.pref_char[node] = s[l]
            self.suff_char[node] = s[l]
            return
        
        mid = (l + r) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        self._build(s, left_child, l, mid)
        self._build(s, right_child, mid + 1, r)
        self._merge(node, left_child, right_child, mid - l + 1, r - mid)

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.pref_char[node] = ch
            self.suff_char[node] = ch
            return
        
        mid = (l + r) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        if idx <= mid:
            self.update(left_child, l, mid, idx, ch)
        else:
            self.update(right_child, mid + 1, r, idx, ch)
        
        self._merge(node, left_child, right_child, mid - l + 1, r - mid)


class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = SegmentTree(s)
        ans = []
        
        for idx, ch in zip(queryIndices, queryCharacters):
            tree.update(1, 0, n - 1, idx, ch)
            ans.append(tree.max_len[1])
            
        return ans