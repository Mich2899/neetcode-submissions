class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counterRed = 0
        counterWhite = 0
        counterBlue = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                counterRed += 1
            elif nums[i] == 1:
                counterWhite += 1
            else:
                counterBlue += 1

        j = 0
        while counterRed!=0:
            nums[j] = 0
            j+=1
            counterRed-=1

        while counterWhite!=0:
            nums[j] = 1
            j+=1
            counterWhite-=1

        while counterBlue!=0:
            nums[j] = 2
            j+=1
            counterBlue-=1