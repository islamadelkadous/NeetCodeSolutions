class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxH = 0
        while l < r:
            currH = min(heights[l], heights[r]) * (r - l)
            if currH > maxH:
                maxH = currH
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxH
        
        
