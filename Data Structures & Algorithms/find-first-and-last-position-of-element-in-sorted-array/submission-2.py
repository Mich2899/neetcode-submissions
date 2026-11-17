class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0 
        high = len(nums) - 1
        first_occ = -1
        last_occ = -1
        n = len(nums)

        #edge cases
        #1st element greater than target
        #last element less than target
        if (len(nums) == 0) or (nums[low] > target) or (nums[high] < target):
            return [-1,-1]

        #Find first occurance
        while(low<=high):
            mid = low + (high - low)//2
            if (nums[mid]==target):
                if(mid == 0 or (nums[mid-1] < nums[mid])):
                    first_occ = mid
                    break
                else:
                    high = mid - 1
            elif (nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
                    
        #Find last occurance
        low = first_occ
        high = len(nums) - 1
        while (low<=high):
            mid = low + (high - low)//2
            if (nums[mid]==target):
                if(mid == n - 1 or (nums[mid] < nums[mid+1])):
                    last_occ = mid
                    break
                else:
                    low  = mid + 1                   
            elif (nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        return [first_occ, last_occ]