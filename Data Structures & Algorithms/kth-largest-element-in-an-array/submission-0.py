class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_num = []
        n_heap = 0
        for nn in nums:
            heapq.heappush(heap_num, nn)
            n_heap += 1
            if n_heap > k:
                heapq.heappop(heap_num)
                n_heap -= 1
        return heap_num[0]