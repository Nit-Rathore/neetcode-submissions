class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            char = s[i]
            
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack[-1]!= "[":
                    substring = stack.pop() + substring 
                
                stack.pop()
            
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k)*substring)
        
        return "".join(stack)