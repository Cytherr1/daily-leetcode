from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = -1
        l, r = 0, 1

        while l != len(s) - 1:
            map = Counter(s[l:r])
            maxE = max(map.values())

            if (r - l + 1) - maxE == k:
                print(s[l:r])
                res = max(res, (r - l + 1))

            if r != len(s):
                r += 1
            else:
                l += 1

        return res
    
nums = [1, 2, 3, 4, 5, 6, 7]
print(nums[6:7])