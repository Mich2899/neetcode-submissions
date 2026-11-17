class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]*len(nums)
        reverse = [1]*len(nums)
        product[0] = 1

        for i in range(1, len(nums)):
            product[i] = product[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            reverse[i] = reverse[i+1] * nums[i+1]
            product[i] = product[i] * reverse[i]

        return product