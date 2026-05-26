class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        for i in range(0,k):
            nums.insert(0,nums[n-1])
            nums.pop(n)
        
        