class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        langesh = 0 

        for n in nums:
            if (n-1) not in arr: 
                length = 0
                while(n+length) in arr:
                    length+=1
                
                langesh = max(length, langesh)
            
        
        return langesh