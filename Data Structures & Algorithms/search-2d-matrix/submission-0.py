class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = sum(matrix, [])
        start,end = 0, len(flat_list)-1
        while(start<=end):
            mid = start + ((end-start)//2)
            if flat_list[mid]==target:
                return True

            elif flat_list[mid]>target:
                end = mid-1
            
            else: start = mid+1
        return False
