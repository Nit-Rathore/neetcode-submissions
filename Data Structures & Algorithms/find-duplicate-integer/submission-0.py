class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i])
            if nums[index]<0: return index 
            nums[index]*=-1
        
        return 0