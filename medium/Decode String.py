class Solution:
    def decodeString(self, s: str) -> str:
        code = ""
        numstack = ""

        for i, e in enumerate(s):
            if ord(e) <= 122 and 97 <= ord(e):
                code = code + "'{}'".format(e)
            elif e == "[" :
                code = code + " + {} * ".format(numstack)
                code = code + "("
                numstack = ""
            elif e == "]":
                code = code + ")"
                if i != len(s) - 1 and s[i + 1] != "]":
                    code = code + " + "
            else:
                numstack = numstack + "{}".format(e)
        
        return eval(code)