import bisect

class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(s):
            return s.count(min(s))
        
        # Precompute and sort the frequencies of all words
        words_freq = sorted(f(w) for w in words)
        n = len(words_freq)
        
        res = []
        for q in queries:
            target = f(q)
            # Find the first index where element > target
            idx = bisect.bisect_right(words_freq, target)
            res.append(n - idx)
            
        return res