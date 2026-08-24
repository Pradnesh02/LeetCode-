class Solution(object):
    def findAnagrams(self, s, p):
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26
        
        for i in range(len_p):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
            
        res = []
        if s_count == p_count:
            res.append(0)
            
        for i in range(len_p, len_s):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len_p]) - ord('a')] -= 1
            
            if s_count == p_count:
                res.append(i - len_p + 1)
                
        return res