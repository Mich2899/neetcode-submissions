class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_dict = {}

        for i in range(0,len(s)):
            if s[i] in iso_dict:
                if iso_dict[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in iso_dict.values():
                    return False 
                else:
                    iso_dict[s[i]] = t[i]

        return True
