class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # 1. Maximize 'a'
        s_a = s
        for ch in s:
            if ch != '9':
                s_a = s.replace(ch, '9')
                break
        a = int(s_a)
        
        # 2. Minimize 'b'
        s_b = s
        if s[0] != '1':
            s_b = s.replace(s[0], '1')
        else:
            for ch in s[1:]:
                if ch not in ('0', '1'):
                    s_b = s.replace(ch, '0')
                    break
        b = int(s_b)
        
        return a - b