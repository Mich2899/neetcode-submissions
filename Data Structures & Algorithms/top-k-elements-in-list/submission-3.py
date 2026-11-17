class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        kv_dict = defaultdict(int)

        for i in nums:
                kv_dict[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in kv_dict.items():
            buckets[value].append(key)
            
        return_list=[]

        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                return_list.append(num)

                if (len(return_list)) == k:
                    return return_list

        return return_list
        