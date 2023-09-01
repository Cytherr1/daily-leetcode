class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0

        romandict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for index, char in enumerate(s):

            if index + 1 < len(s):

                if char == "I" and (s[index + 1] == "V" or s[index + 1] == "X"):
                    number -= 1

                elif char == "X" and (s[index + 1] == "L" or s[index + 1] == "C"):
                    number -= 10

                elif char == "C" and (s[index + 1] == "D" or s[index + 1] == "D"):
                    number -= 100

                else:
                    number += romandict[char]

            else:
                number += romandict[char]

        return number
 