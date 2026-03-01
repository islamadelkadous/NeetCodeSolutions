class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 1
        result = [0] * len(temperatures)
        while l < len(temperatures) and r < len(temperatures):
            if temperatures[l] < temperatures[r]:
                result[l] = r - l
                l += 1
                r = l + 1
            elif r == len(temperatures) - 1:
                result[l] = 0
                l += 1
                r  = l + 1
            else:
                r += 1
        
        return result
        
