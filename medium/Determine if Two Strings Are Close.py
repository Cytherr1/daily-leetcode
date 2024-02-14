from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hmW1, hmW2 = Counter(word1), Counter(word2)
        
        return True if sorted(hmW1.values()) == sorted(hmW2.values()) and set(hmW1.keys()) == set(hmW2.keys()) else False