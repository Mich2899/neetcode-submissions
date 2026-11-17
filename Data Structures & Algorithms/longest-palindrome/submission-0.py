class Solution:
    def longestPalindrome(self, s: str) -> int:
        myhashset = set()
        count = 0 

        for i in range(len(s)):
            if s[i] in myhashset:
                myhashset.remove(s[i])
                count += 2
            else:
                myhashset.add(s[i])

        if myhashset:
            count += 1

        return count
