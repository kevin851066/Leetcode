import heapq

class KthLargest:

    def __init__(self, k, nums):
        '''
        type: k: int
        type: nums: List[int]
        '''
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k: # avoid nums is empty at first
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)