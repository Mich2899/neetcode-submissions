class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = [] #O(n) time complexity
        lookup = {}
         
        for i in range(0, len(nums)):
            lookup[nums[i]] = 1

        for i in range (1, len(nums)+1):
            if i in lookup:
                continue
            else:
                missing.append(i)

        return missing