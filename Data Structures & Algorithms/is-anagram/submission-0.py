class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A = list(s)
        B = list(t)
        A.sort()
        B.sort()

        if A == B:
            return True
        else:
            return False