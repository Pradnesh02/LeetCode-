class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def getMaxWindow(target_char):
            left = 0
            max_len = 0
            count = 0  # Number of target_char characters in the current window
            
            for right in range(len(answerKey)):
                if answerKey[right] == target_char:
                    count += 1
                
                # Shrink window if count exceeds k
                while count > k:
                    if answerKey[left] == target_char:
                        count -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len

        # Maximum consecutive answers by changing at most k 'F's to 'T's
        # OR changing at most k 'T's to 'F's
        return max(getMaxWindow('F'), getMaxWindow('T'))