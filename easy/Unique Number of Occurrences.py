from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        hm = Counter(arr)
        return True if len(arr) == sum(list(set(hm.values()))) else False
       