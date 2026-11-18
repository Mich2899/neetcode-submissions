class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        onceXor = 0

        for i in range(0, len(nums)):
            onceXor ^= nums[i]

        return onceXor