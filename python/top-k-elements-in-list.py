class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = []
        for num, count in counter.items():
            arr.append([count, num])

        arr.sort()
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
