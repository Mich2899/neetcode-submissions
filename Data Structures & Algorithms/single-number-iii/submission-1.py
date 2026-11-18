class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        element1 = 0
        twoXor = 0

        #1) XOR whole list, this gives Xor of the two non repeating elements
        for i in range(0, len(nums)):
            twoXor ^= nums[i]

        #2) 2's compliment of the resulting twoXor value
        twosComp = (~(twoXor)+1)

        #3) AND 1 and 2
        andArr = twoXor & twosComp

        #4) iterate through the array and save the elements that result in 1 after anding with step 3 and Xor them
        for i in range(0, len(nums)):
            if(andArr & nums[i]):
                element1 ^= nums[i]

        #5) find 2nd element by xoring with the resultant Xor in step1
        element2 = twoXor ^ element1

        return [element1, element2]