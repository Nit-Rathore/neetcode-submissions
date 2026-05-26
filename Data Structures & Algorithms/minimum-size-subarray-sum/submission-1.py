class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        r = l = subArray = 0
        res = n+1

        while r < n:
            while subArray < target and r<n:
                subArray+= nums[r]
                r+=1
 
            while subArray >= target:
                subArray -= nums[l]
                l+=1
            
            res = min(res,r-l+1)
        
        return res if res!=n+1 else 0