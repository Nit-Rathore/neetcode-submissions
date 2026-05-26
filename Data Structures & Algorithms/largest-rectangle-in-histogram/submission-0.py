class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left, right = [-1]*n,[n]*n
        
        for i in range(n):
            if stack and heights[stack[-1]]<heights[i]:
                left[i] = stack[-1]
            
            elif stack and heights[stack[-1]]>=heights[i]:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                
                if stack: 
                    left[i] = stack[-1]
            
            stack.append(i)

        stack = []
        
        for i in range(n-1,-1,-1):
            if stack and heights[stack[-1]]<heights[i]:
                right[i] = stack[-1]
            
            elif stack and heights[stack[-1]]>=heights[i]:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                
                if stack:
                    right[i] = stack[-1]
                
            stack.append(i)
        
        maxArea = 0
        for i in range(n):
            width = right[i]-left[i]-1
            area = heights[i]*width 
            maxArea = max(maxArea,area)

        return maxArea   
 