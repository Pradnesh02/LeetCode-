class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        # path_len[depth] stores cumulative path length up to depth level
        path_len = {-1: 0}
        
        for line in input.split('\n'):
            # Depth is determined by count of leading tab characters
            depth = line.count('\t')
            # Extract actual file/dir name by stripping '\t'
            name = line.lstrip('\t')
            
            if '.' in name:
                # It's a file: calculate absolute path length
                # path_len[depth - 1] + 1 (for '/') + len(name)
                # For depth 0: path_len[-1] + 0 + len(name) = len(name)
                current_len = path_len[depth - 1] + (1 if depth > 0 else 0) + len(name)
                max_len = max(max_len, current_len)
            else:
                # It's a directory: store cumulative path length at this depth
                path_len[depth] = path_len[depth - 1] + (1 if depth > 0 else 0) + len(name)
                
        return max_len