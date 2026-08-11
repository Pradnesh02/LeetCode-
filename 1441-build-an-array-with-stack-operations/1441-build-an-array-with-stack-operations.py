class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        operations = []
        target_idx = 0
        curr = 1
        
        while target_idx < len(target):
            operations.append("Push")
            
            # If current stream number is in target, keep it
            if curr == target[target_idx]:
                target_idx += 1
            # If current stream number is not needed, pop it out
            else:
                operations.append("Pop")
                
            curr += 1
            
        return operations