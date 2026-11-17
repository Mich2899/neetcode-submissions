class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while(mid<=high):
            if (nums[mid]==0):
                #swap(mid, low)
                #mid++, low++
                tmp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = tmp

                low+=1
                mid+=1
            elif (nums[mid]==1):
                #mid++
                mid+=1
            else: #nums[mid]==2
                #swap(mid, high)
                #high--
                tmp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = tmp
                high-=1


        