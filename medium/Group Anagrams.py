class Solution:
    def groupAnagrams(self, strs):

        seen = [False] * len(strs)
        groups = []
        hashes = []

        for i in strs:
            dictI = {x: i.count(x) for x in set(i)}
            hashes.append(dictI)
        
        unique = [dict(t) for t in {tuple(d.items()) for d in hashes}]

        for i in unique:
            group = []
            for j, e in enumerate(hashes):
                if e == i and not seen[j]:
                    group.append(strs[j])
                    seen[j] = True
            if group:
                groups.append(group)
                
        return groups