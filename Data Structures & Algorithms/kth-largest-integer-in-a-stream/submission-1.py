class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kth_list = nums
        self.len_lst = len(self.kth_list)
        heapq.heapify(self.kth_list)
        for _ in range(self.len_lst-k):
            heapq.heappop(self.kth_list)

    def add(self, val: int) -> int:
        if self.len_lst < self.k:
            heapq.heappush(self.kth_list, val)
            self.len_lst+=1
        elif val > self.kth_list[0]:
            heapq.heapreplace(self.kth_list, val)
        return self.kth_list[0]