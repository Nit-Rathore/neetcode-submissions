class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            n = len(s2)
            m = len(s1)
            s = sorted(s1)
            l=0

            for r in range(m-1,n):
                if s2[l] in s1:
                    word = s2[l:r+1]
                    if sorted(word) == s: return True 
                l+=1

            return False


                    
