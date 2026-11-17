class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Time: O(n^2) Space:O(1)

        #Time: O(nlogn)
        nums.sort()
        triplet_list = []
        i = 0
        
        for i in range(0, len(nums)-2):
            if (i>0) and (nums[i]==nums[i-1]):
                continue
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if (nums[left] + nums[right]) < target : 
                    left += 1
                elif (nums[left] + nums[right]) > target:
                    right -= 1
                else:
                    triplet_list.append([nums[i],nums[left],nums[right]])  
                    prevleft = left
                    prevright = right
                    while((left<len(nums) - 1) and (nums[left] == nums[prevleft])):
                        left += 1                    
                    while((right>0) and (nums[right] == nums[prevright])):
                        right -=1
            
        return triplet_list