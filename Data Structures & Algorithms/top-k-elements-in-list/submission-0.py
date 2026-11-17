class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        kv_dict = defaultdict(int)
        
        for i in range(0, len(nums)):
            key = nums[i]
            if key not in kv_dict:
                kv_dict[key] = 1
            else:
                kv_dict[key] += 1

        values_list = list(kv_dict.values())

        largest_k = sorted(values_list, reverse=True)[:k]

        return [key for key, values in kv_dict.items() if values in largest_k]



