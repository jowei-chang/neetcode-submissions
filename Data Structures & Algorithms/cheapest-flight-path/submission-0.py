class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = [(0,src,1)]      # (cost, source, stop)
        adj = collections.defaultdict(dict)
        for srci, desti, pricei in flights:
            adj[srci][desti] = pricei
        visited = collections.defaultdict(list)
        while heap:
            cost, cur, stop = heapq.heappop(heap)
            if cur==dst: return cost
            if cur in visited and visited[cur]<=stop:
                continue
            visited[cur] = stop
            
            if stop>=k+2: continue
            for dest in adj[cur].keys():
                heapq.heappush(heap, (cost+adj[cur][dest], dest, stop+1))
        return -1