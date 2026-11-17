class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso_dict = {}
        list_s = list(s)
        list_t = list(t)

        for key, value in zip(list_s, list_t):
            if key in iso_dict:
                if iso_dict[key] == value:
                    continue
                else:
                    return False
            else:
                if value in iso_dict.values():
                    return False 
                else:
                    iso_dict[key] = value

        return True
