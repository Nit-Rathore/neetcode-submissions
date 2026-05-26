class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        if n==1 or k==1:
            return nums

        for r in range(n-k+1):
            Nummax = 0
            
            for l in range(r,r+k):
                if l >=n: break 
                Nummax = max(nums[l], Nummax)
            

            res.append(Nummax)
        
        return res

