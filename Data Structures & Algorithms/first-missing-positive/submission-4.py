class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        if 1 not in nums: 
            return 1

        for i in range(n):
            if nums[i] <=0 or nums[i]>n:
                nums[i] =1
        
        nums[0]*=-1
                
        for i in range(n):
            index = abs(nums[i])
            if index<n and nums[index]>0:
                nums[index] = nums[index] * -1
            
        for i in range(1,n):
            if nums[i]>0:
                return i
        
        print(nums)

        if -n in nums:
            return n+1
        
        return n
        