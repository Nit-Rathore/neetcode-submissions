from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]

        for i in nums: 
            hashmap[i] = hashmap.get(i,0) + 1
        
        for key, val in hashmap.items():
            freq[val].append(key)
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)        

        return res[:k]
