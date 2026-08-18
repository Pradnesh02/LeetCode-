class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = max(self.tree[node], val)
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res = max(res, self.query(2 * node, l, mid, ql, qr))
        if qr > mid:
            res = max(res, self.query(2 * node + 1, mid + 1, r, ql, qr))
        return res


class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        st = SegmentTree(max_val)
        
        for x in nums:
            left_bound = max(1, x - k)
            right_bound = x - 1
            
            if left_bound <= right_bound:
                best_prev = st.query(1, 1, max_val, left_bound, right_bound)
            else:
                best_prev = 0
                
            cur_len = best_prev + 1
            st.update(1, 1, max_val, x, cur_len)
            
        return st.tree[1]