class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if (nums[i] + nums[j] == target and i!=j):
                    res.extend([i,j])
                    break
        
        return res
