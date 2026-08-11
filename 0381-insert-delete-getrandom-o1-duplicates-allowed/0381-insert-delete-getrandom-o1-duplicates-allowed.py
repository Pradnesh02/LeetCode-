from collections import defaultdict
import random

class RandomizedCollection(object):

    def __init__(self):
        self.nums = []
        self.val_to_indices = defaultdict(set)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        is_not_present = len(self.val_to_indices[val]) == 0
        
        # Store index in the set corresponding to val
        self.val_to_indices[val].add(len(self.nums))
        self.nums.append(val)
        
        return is_not_present

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not self.val_to_indices[val]:
            return False
            
        # Get an index to remove and the last value/index in the list
        remove_idx = self.val_to_indices[val].pop()
        last_idx = len(self.nums) - 1
        last_val = self.nums[-1]
        
        # If the element to remove is NOT the last element in the array
        if remove_idx != last_idx:
            # Overwrite the element to remove with the last element
            self.nums[remove_idx] = last_val
            # Update index tracking for last_val
            self.val_to_indices[last_val].remove(last_idx)
            self.val_to_indices[last_val].add(remove_idx)
            
        # Remove the last element
        self.nums.pop()
        
        # Clean up empty sets
        if not self.val_to_indices[val]:
            del self.val_to_indices[val]
            
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)