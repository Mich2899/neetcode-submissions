class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        kv_dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in kv_dict:
                kv_dict[key] = []

            kv_dict[key].append(word)

        return list(kv_dict.values())        