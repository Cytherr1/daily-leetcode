class Solution:
    def largestAltitude(self, gain) -> int:
        gain.insert(0, 0)
        h = int()

        for i in range(1, len(gain)):
            gain[i] = gain[i - 1] + gain[i]
            h = max(h, gain[i])

        return h