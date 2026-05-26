class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        res =0

        if r<1:
            return r+1

        while (l<=r):
            weight = people[l] + people[r]
            if weight <= limit:
                res+=1
                l+=1
                r-=1
            else:
                res+=1
                r-=1
            
        return res
       