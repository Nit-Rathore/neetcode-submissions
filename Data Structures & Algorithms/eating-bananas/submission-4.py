class Solution:
    def isBananaOver(self, piles:List[int], rate:int, h:int) -> boolean:
        hours=0
        
        for i in piles:
            curHour = int(math.ceil(i/rate))
            hours+=curHour

        return hours<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        
        while l<=r:
            rate = (l+r)//2

            if self.isBananaOver(piles,rate,h):
                res = min(rate,res)
                r = rate -1 
            else:
                l = rate+1 
            
        return res 
