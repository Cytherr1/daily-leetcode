import bisect

class Solution:
    def fullBloomFlowers(self, flowers, people):
        
        (beg, end) = map(sorted, zip(*flowers))
        ans  = []

        for p in people:
            ans.append(bisect.bisect_right(beg, p) - bisect.bisect_left(end, p))

        return ans
