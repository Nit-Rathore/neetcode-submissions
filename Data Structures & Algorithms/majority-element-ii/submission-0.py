class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        size = len(nums)//3
        res = []

        for n in nums: 
            count[n]+=1

            if len(count)<=2:
                continue

            new_count = defaultdict(int) 
            for n,c in count.items():
                if c > 1:
                    new_count[n] = c-1
                

            count = new_count
        

        for n,c in count.items():
            if nums.count(n) > size:
                res.append(n)
        
        return res        