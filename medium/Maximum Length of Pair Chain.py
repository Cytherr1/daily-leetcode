class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        chain = [min(pairs, key= lambda x : x[1])]
        p = chain[0][1]

        while pairs:
            m = min(pairs, key= lambda x : x[1])

            if m[0] > p:
                p = m[1]
                chain.append(m)
            
            pairs.remove(m)
        
        return len(chain)
