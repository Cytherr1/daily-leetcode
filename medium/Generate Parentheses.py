class Solution:
    def generateParenthesis(self, n):
        combs = []

        def formString(n, s=""):
            if s == "":
                formString(n-1, "(")
            else:
                if s.count("(") == s.count(")"):
                    if n == 0:
                        combs.append(s)
                    else:
                        s += "("
                        formString(n-1, s)
                elif s.count("(") > s.count(")"):
                    if n == 0:
                        s += ")"
                        formString(n, s)
                    else:
                        formString(n, s + ")")
                        formString(n-1, s + "(")
        formString(n)
        
        return combs