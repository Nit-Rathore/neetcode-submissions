class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}

        for character in s: 
            if character in pair: 
                if stack and stack[-1] == pair[character]:
                    stack.pop()
                else: return False 
            
            else: 
                stack.append(character)         
            
        return True if not stack else False 