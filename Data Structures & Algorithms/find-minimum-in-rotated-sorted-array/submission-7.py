class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        n = len(nums)

        while (low <= high):
            mid = low + (high - low)//2
            #check if mid is lowest return mid
            if ((mid == 0) or nums[mid-1] > nums[mid]) and (mid == (n - 1) or nums[mid+1] > nums[mid]):
                return nums[mid]
            #check if left is sorted
            elif (nums[mid] >= nums[low]):
                if (nums[mid] < nums[high]):
                    #if both are sorted go to left 
                    high = mid - 1
                else:
                    #else go to right
                    low = mid + 1
            #right is sorted
            else:
                high = mid - 1

        

