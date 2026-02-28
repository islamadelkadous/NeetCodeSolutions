class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = s2[:len(s1)]
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if sorted(window) == sorted(s1):
                return True
            window = window[1:]
            l+=1
            r+=1
            if r < len(s2):
                window = window + s2[r]
        
        return False
