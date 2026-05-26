class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            length = len(s)
            res += str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Step 1: find length
            length = 0
            while s[i] != '#':
                length = length * 10 + int(s[i])
                i += 1

            # skip '#'
            i += 1

            # Step 2: extract string
            res.append(s[i:i+length])

            # move pointer ahead
            i += length

        return res