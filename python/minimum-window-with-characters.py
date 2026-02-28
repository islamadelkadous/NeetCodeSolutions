class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterMap = Counter(t)
        cost = len(t)
        sol = ''
        for i in range(len(s)):
            if counterMap[s[i]] > 0:
                currMap = counterMap.copy()
                currIndex = i
                currCost = cost
                currSol = ''
                while currIndex < len(s):
                    if currMap[s[currIndex]] > 0:
                        currMap[s[currIndex]] -= 1
                        currCost -= 1
                    currSol += s[currIndex]
                    if currCost == 0 and (len(sol) == 0 or len(sol) > len(currSol)):
                        sol = currSol
                    currIndex += 1
        
        return sol



        
