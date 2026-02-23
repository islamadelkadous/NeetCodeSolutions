class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l, r, maxL = 0, 0, 0
        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            
            hashSet.add(s[r])
            r += 1
            maxL = max(r - l, maxL)
        
        return maxL
