class Solution:
    
    def isShip(self, weights:List[int], days:int, cap:int) -> boolean:
        day = 1
        currCap = cap

        for w in weights:
            if currCap - w <0:
                day+=1
                currCap = cap
            currCap -= w
        
        return day<=days

    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r

        while l<=r:
            cap = (l+r)//2

            if self.isShip(weights,days,cap):
                res = min(res,cap)
                r = cap-1
            else: 
                l = cap+1

        return res 
        
        