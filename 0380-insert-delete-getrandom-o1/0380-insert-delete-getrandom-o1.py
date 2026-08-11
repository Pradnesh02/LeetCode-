import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.val_to_idx = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False
            
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_idx:
            return False
            
        # Get index of item to remove and value of last item
        idx_to_remove = self.val_to_idx[val]
        last_val = self.nums[-1]
        
        # Swap last element with the element to remove
        self.nums[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove
        
        # Remove last element
        self.nums.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)