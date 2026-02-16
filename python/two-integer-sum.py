class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, val in enumerate(nums):
            curr = target - val
            if curr in prevMap:
                return [prevMap[curr], i]
            prevMap[val] = i

        
