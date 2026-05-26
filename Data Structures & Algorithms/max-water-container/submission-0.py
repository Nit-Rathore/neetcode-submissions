class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0, n-1
        maxArea = 0
        while l<r:
            area = (r-l)*min(heights[r], heights[l])
            
            if heights[r] < heights[l]:
                r-=1
            else: 
                l+=1
            
            maxArea = max(area, maxArea)
        
        return maxArea