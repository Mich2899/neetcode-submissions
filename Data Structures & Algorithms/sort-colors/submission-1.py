class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counterred = 0
        counterwhite = 0
        counterblue = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                counterred += 1
            elif nums[i] == 1:
                counterwhite += 1
            else:
                counterblue += 1

        j = 0
        while j <(counterred):
            nums[j] = 0
            j+=1

        k = j
        while k<(j+counterwhite):
            nums[k] = 1
            k+=1

        l = k
        while l<(k+counterblue):
            nums[l] = 2
            l+=1