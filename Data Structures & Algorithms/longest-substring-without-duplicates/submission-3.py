class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        maxL,l,r,n = 0,0,0,len(s)
        if n ==1:
            return 1

        while r<n:
            if s[r] not in hashSet:
                hashSet.add(s[r])
                r+=1
            
            else: 
                length = len(hashSet)
                maxL = max(maxL,length)
                hashSet.discard(s[l])
                l+=1
        
        return max(maxL, len(hashSet))