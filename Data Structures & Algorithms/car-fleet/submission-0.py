class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        stack = []
        for p,s in zip(position,speed):
            dist = target-p
            hashmap[dist] = s
        
        hashmap = dict(sorted(hashmap.items()))
        print(hashmap)

        for p,s in hashmap.items():
            time = p/s
            if stack and time>stack[-1]:
                stack.append(time)
            elif stack and time<=stack[-1]:
                continue 
            if not stack: 
                stack.append(time)
        
        return len(stack)


            