class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(fly_map, airport):
            while airport in fly_map and fly_map[airport]:
                dest = fly_map[airport].pop(0)
                dfs(fly_map, dest)
            self.res.append(airport)

        adj = {}
        for src, dest in tickets:
            if src not in adj:
                adj[src] = [dest]
            else:
                adj[src].append(dest)
        for ad in adj:
            adj[ad].sort()
        self.res = []
        
        dfs(adj, "JFK")
        return self.res[::-1]