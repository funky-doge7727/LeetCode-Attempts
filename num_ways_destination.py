#problem 1976: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        def dijkstra():
            pq = [(0, 0)]
            dist[0] = 0
            counts[0] = 1
            while pq:
                d, u = heappop(pq)
                if d > dist[u]: continue
                for v, w in AL[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        counts[v] = counts[u]
                        heappush(pq, (dist[v], v))
                    elif dist[u] + w == dist[v]:
                        counts[v] += counts[u]
                        
        AL = [[] for _ in range(n)] 

        for u, v, w in roads:
            AL[u].append((v, w))
            AL[v].append((u, w))

        dist = [float("inf")] * n
        counts = [0] * n
        dijkstra()
        return counts[n-1] % (10**9+7)
