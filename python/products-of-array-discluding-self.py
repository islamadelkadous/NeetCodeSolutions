class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerosCount = 0
        totalProduct = 1
        for n in nums:
            if n == 0:
                zerosCount += 1
                if zerosCount > 1:
                    return [0] * len(nums)
            else:
                totalProduct *= n
        
        output = []
        for n in nums:
            if n == 0:
                output.append(totalProduct)
            elif zerosCount > 0:
                output.append(0)
            else:
                output.append(totalProduct//n)
        return output
        
