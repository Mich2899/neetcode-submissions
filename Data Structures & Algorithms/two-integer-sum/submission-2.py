class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum_hashmap = {}
        i1 = 0
        i2 = 0

        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in twosum_hashmap:
                i1 = twosum_hashmap[remainder]
                i2 = i
            else:
                twosum_hashmap[nums[i]] = i
        
        return [i1,i2]
