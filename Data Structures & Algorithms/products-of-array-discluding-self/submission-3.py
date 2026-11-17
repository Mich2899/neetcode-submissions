class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]*len(nums)
        product[0] = 1
        runprod = 1

        for i in range(1, len(nums)):
            product[i] = product[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            runprod = runprod * nums[i+1]
            product[i] = product[i] * runprod

        return product       