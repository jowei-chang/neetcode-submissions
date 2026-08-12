class MedianFinder:

    def __init__(self):
        self.buf_large = []     # min-heap
        self.buf_small = []     # max-heap
        self.n_large = 0
        self.n_small = 0

    def addNum(self, num: int) -> None:
        if self.n_large + self.n_small < 2:
            if self.n_large + self.n_small==0:
                heapq.heappush(self.buf_small, -num)
                self.n_small += 1
            else:       # self.n_large + self.n_small = 1
                if num >= -self.buf_small[0]:
                    heapq.heappush(self.buf_large, num)
                else:
                    tmp = -heapq.heappop(self.buf_small)
                    heapq.heappush(self.buf_small, -num)
                    heapq.heappush(self.buf_large, tmp)
                self.n_large += 1
        elif self.n_small>self.n_large:
            if num >= -self.buf_small[0]:
                heapq.heappush(self.buf_large, num)
            else:
                tmp = -heapq.heappop(self.buf_small)
                heapq.heappush(self.buf_small, -num)
                heapq.heappush(self.buf_large, tmp)
            self.n_large += 1
        elif self.n_small<self.n_large:
            if num <= self.buf_large[0]:
                heapq.heappush(self.buf_small, -num)
            else:
                tmp = heapq.heappop(self.buf_large)
                heapq.heappush(self.buf_large, num)
                heapq.heappush(self.buf_small, -tmp)
            self.n_small += 1
        else:       # n_small = n_large
            if -self.buf_small[0] >= num:       # num <= max(small)
                heapq.heappush(self.buf_small, -num)
                self.n_small += 1
            elif num >= self.buf_large[0]:      # min(large) <= num
                heapq.heappush(self.buf_large, num)
                self.n_large += 1
            else:                               # max(small) < num < min(large)
                heapq.heappush(self.buf_small, -num)
                self.n_small += 1

    def findMedian(self) -> float:
        if self.n_large > self.n_small:
            return self.buf_large[0]
        elif self.n_large < self.n_small:
            return -self.buf_small[0]
        else:       # n_large = n_small
            return (self.buf_large[0]-self.buf_small[0])/2.0
        