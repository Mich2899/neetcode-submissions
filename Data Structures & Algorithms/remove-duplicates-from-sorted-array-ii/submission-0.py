class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        k = 0
        count = 1 

        while(right<len(nums)):
            if nums[left] == nums[right]:
                left+=1
                right+=1
                count+=1
            else:
                if count>1:
                    nums[k] = nums[left]
                    nums[k+1] = nums[left]
                    k+=2
                else:
                    nums[k] = nums[left]
                    k+=1
                left = right
                right+=1
                count = 1

        if(count>1):
            nums[k] = nums[left]
            nums[k+1] = nums[left]
            k+=1
        else:
            nums[k] = nums[left]

        return k+1       