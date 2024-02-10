class Solution:
    def reverseWords(self, s: str) -> str:
        words, res = s.split(" "), ""
        for i in words[::-1]:
            if i != "":
                res += i + " "

        return res.strip()