class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w = "" 
        l = min(len(word1), len(word2))
        s = max(len(word1), len(word2))

        for i in range(l):
           w += word1[i]
           w += word2[i]
        
        if len(word1) == s:
            w += word1[l:s]
        else:
            w += word2[l:s]

        return w

        
           
