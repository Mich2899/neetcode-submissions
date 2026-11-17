class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = [] #o(n^2) time complexity

        for i in range (1, len(nums)+1):
            if i in nums:
                continue
            else:
                missing.append(i)

        return missing