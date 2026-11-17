from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        frequency  = {}
        #keys = elements, value = freq of elements

        frequency = Counter(nums)
        runningsum = [0] * (max(nums) + 1)
        
        for i in range(0, max(frequency.keys()) + 1):
            if i in frequency.keys():
                runningsum[i] = i * frequency[i]

        dp = [0] * len(runningsum) 
        dp[0] = runningsum[0]
        dp[1] = max(runningsum[1], dp[0])

        for i in range(2, len(runningsum)):
            dp[i] = max(dp[i-1], dp[i-2] + runningsum[i])

        return max(dp)
