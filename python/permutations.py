class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

        def backtracking():
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking()
                    curr.pop()
        
        backtracking()
        return res
            
            
            
            
        
