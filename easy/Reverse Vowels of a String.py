class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a" ,"e", "o", "i", "u", "A", "E", "O", "I", "U"]
        sv = [i for i in s if i in vowels]
        sv = sv[::-1]

        n = ""
        x = 0

        for i in s:
            if i in vowels:
                n += sv[x]
                x += 1
            else:
                n += i
        
        return n


