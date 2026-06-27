class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        res = nums[0]
        if len(nums)==1: return res

        for i in nums: 
            if count ==0: 
                res = i 
            
            if i == res: count+=1
            if i!= res: count -=1
        
        return res 
        