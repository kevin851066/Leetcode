import heapq

class Solution:
    def lastStoneWeight(self, stones):
        '''
        type: stones: List[int]
        rtype: int
        '''
        stones = [(-1) * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
                
        return 0 if len(stones) == 0 else -stones[0]
                