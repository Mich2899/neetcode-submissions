class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]*len(nums)
        result = 1 
        zero_flag = 0

        for i in range(0, len(nums)):
            if nums[i]!=0:
                result *= nums[i]
            else:
                zero_flag += 1

        for i in range(0, len(nums)):
            if (nums[i] != 0) and (zero_flag==0):
                product[i] = result//nums[i]
            elif (nums[i] != 0) and (zero_flag==1):
                product[i] = 0
            elif(zero_flag>1):
                product[i] = 0
            else:
                product[i] = result

        return product
