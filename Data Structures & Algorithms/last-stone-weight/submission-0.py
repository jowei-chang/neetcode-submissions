class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for ss in stones:
            heapq.heappush(stone_heap, -ss)
        n_stone = len(stones)
        while n_stone > 1:
            y = heapq.heappop(stone_heap)
            x = heapq.heappop(stone_heap)
            n_stone -= 2
            if x!=y:
                heapq.heappush(stone_heap, y-x)
                n_stone += 1
        if stone_heap:
            return -stone_heap[0]
        return 0