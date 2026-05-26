class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = res = 0
        count = {0:1}
        
        for n in nums:
            prefixSum +=n
            diff = prefixSum - k

            if diff in count.keys():
                res += count[diff]
            
            count[prefixSum]= 1 + count.get(prefixSum,0)

        return res

