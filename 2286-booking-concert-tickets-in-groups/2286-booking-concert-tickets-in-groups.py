class BookMyShow(object):

    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """
        self.n = n
        self.m = m
        self.tree_sum = [0] * (4 * n)
        self.tree_max = [0] * (4 * n)
        self.first_available_row = 0
        self._build(1, 0, n - 1)

    def _build(self, node, l, r):
        if l == r:
            self.tree_sum[node] = self.m
            self.tree_max[node] = self.m
            return
        mid = (l + r) // 2
        self._build(2 * node, l, mid)
        self._build(2 * node + 1, mid + 1, r)
        self._pushup(node)

    def _pushup(self, node):
        self.tree_sum[node] = self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]
        self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])

    def _update(self, node, l, r, idx, val):
        if l == r:
            self.tree_sum[node] = val
            self.tree_max[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self._update(2 * node, l, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, r, idx, val)
        self._pushup(node)

    def _query_sum(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree_sum[node]
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += self._query_sum(2 * node, l, mid, ql, qr)
        if qr > mid:
            res += self._query_sum(2 * node + 1, mid + 1, r, ql, qr)
        return res

    def _find_first_row(self, node, l, r, maxRow, k):
        if self.tree_max[node] < k or l > maxRow:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        res = self._find_first_row(2 * node, l, mid, maxRow, k)
        if res != -1:
            return res
        return self._find_first_row(2 * node + 1, mid + 1, r, maxRow, k)

    def gather(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: List[int]
        """
        row = self._find_first_row(1, 0, self.n - 1, maxRow, k)
        if row == -1:
            return []
        
        available = self._query_sum(1, 0, self.n - 1, row, row)
        seat = self.m - available
        self._update(1, 0, self.n - 1, row, available - k)
        return [row, seat]

    def scatter(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: bool
        """
        total_available = self._query_sum(1, 0, self.n - 1, 0, maxRow)
        if total_available < k:
            return False
        
        while k > 0:
            available = self._query_sum(1, 0, self.n - 1, self.first_available_row, self.first_available_row)
            if available == 0:
                self.first_available_row += 1
                continue
                
            take = min(available, k)
            self._update(1, 0, self.n - 1, self.first_available_row, available - take)
            k -= take
            
            if available - take == 0:
                self.first_available_row += 1
                
        return True