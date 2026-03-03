# two pointers
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
        
# monotonic stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        result = [0] * len(temperatures)
        monStack = []
        for i  in range(len(temperatures) - 1, -1, -1):
            while monStack and temperatures[i] >= temperatures[monStack[-1]]:
                monStack.pop()

            if monStack:
                result[i] = monStack[-1] - i

            monStack.append(i)
        
        return result
        
        
