class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = []
        i = 0
        while i < len(s):
            d.append((indices[i],s[i]))            
            i += 1
        d.sort()
        output = ''
        for i in d:
            output += i[-1]
        return output
