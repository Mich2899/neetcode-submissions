class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = {}

        for i in range(0, len(nums)):
                unique[nums[i]]=1

        i = 0
        for keys in unique:
            nums[i] = keys
            i+=1
        
        return i