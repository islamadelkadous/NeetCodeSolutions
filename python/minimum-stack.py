class MinStack:
    stk = []
    minHeap = []

    def __init__(self):
        self.stk = []
        self.minHeap = []

    def push(self, val: int) -> None:
        heapq.heappush(self.minHeap, val)
        self.stk.append(val)
        

    def pop(self) -> None:
        print(self.stk)
        val = self.stk.pop()
        self.minHeap.remove(val)
        heapq.heapify(self.minHeap)
        return val

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minHeap[0]
