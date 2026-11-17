class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = [0]*(len(nums)+1) #O(n) time complexity, O(1) space complexity
        tracker = 0

        for i in range(0, len(nums)):
            missing[nums[i]] = 1

        for i in range(1, len(nums)+1):
            if missing[i] == 0:
                missing[tracker] = i
                tracker+=1

        return missing[0:tracker]


        