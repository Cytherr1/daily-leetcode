class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        x = ""
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                x += i

        return (x == x[::-1])


s = "race a car"
l = s.split()
s = ""
for i in l:
    s += i
print(s)