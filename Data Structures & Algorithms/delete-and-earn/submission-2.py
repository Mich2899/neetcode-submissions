class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq  = [0] * (max(nums) + 1)
        #keys = elements, value = freq of elements
        
        for i in range(0, len(nums)):
            freq[nums[i]] += nums[i]

        dp = [0] * len(freq) 
        dp[0] = freq[0]
        dp[1] = max(freq[1], dp[0])

        for i in range(2, len(freq)):
            dp[i] = max(dp[i-1], dp[i-2] + freq[i])

        return max(dp)
