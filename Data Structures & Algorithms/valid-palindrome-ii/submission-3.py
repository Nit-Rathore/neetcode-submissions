class Solution:
    def validPalindrome(self, s: str) -> bool:
        n= len(s)
        for i in range(n):
            new_string = s[:i] + s[i+1:] 
            if new_string == new_string[::-1]:
                return True

        return False 
        