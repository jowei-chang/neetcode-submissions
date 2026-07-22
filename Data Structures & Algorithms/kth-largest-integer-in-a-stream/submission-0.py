class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.kth_list = nums

    def add(self, val: int) -> int:
        self.kth_list.append(val)
        self.kth_list.sort()
        return self.kth_list[-self.k]