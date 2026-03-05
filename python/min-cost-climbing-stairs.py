class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0
        res = [0, 0]
        for i in range(2, len(cost) + 1):
            res.append(min(cost[i-1] + res[i-1], cost[i-2] + res[i-2]))
        
        return res[-1]

        
