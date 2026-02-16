class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numArr = set()
        for num in nums:
            if num in numArr:
                return True
            numArr.add(num)
        return False

        
