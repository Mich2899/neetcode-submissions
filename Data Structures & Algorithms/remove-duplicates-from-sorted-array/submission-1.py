class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        k = 0

        while(right<len(nums)):
            if nums[left] == nums[right]:
                left+=1
                right+=1
            else:
                nums[k] = nums[left]
                left = right
                right+=1
                k+=1

        nums[k] = nums[left]

        return k+1