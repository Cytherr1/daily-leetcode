class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = senate
        while s:
            if s[0] == "R":
                if s.find("D") >= 0:
                    s = s.replace("D", "", 1)
                    s += "R"
                else:
                    return "Radiant"
            else:
                if s.find("R") >= 0:
                    s = s.replace("R", "", 1)
                    s += "D"
                else:
                    return "Dire"
            s = s[1:]