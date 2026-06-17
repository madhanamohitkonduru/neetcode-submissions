class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        lis = [[] for i in range(len(nums)+1)]
        
        for key, value in hashmap.items():
            lis[value].append(key)

        k_lis = []
        for i in range(len(nums), 0, -1):
            k_lis.extend(lis[i])
            if len(k_lis)==k:
                return k_lis