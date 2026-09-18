class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        star_idx = -1
        match_idx = 0
        
        len_s, len_p = len(s), len(p)
        
        while s_idx < len_s:
            # 1. Direct character match or '?'
            if p_idx < len_p and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            # 2. Encountered a '*' wildcard
            elif p_idx < len_p and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
            # 3. Mismatch occurred, but we have a previous '*' to backtrack to
            elif star_idx != -1:
                match_idx += 1
                s_idx = match_idx
                p_idx = star_idx + 1
            # 4. Mismatch without any previous '*'
            else:
                return False
        
        # Check if remaining characters in pattern are all '*'
        while p_idx < len_p and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len_p