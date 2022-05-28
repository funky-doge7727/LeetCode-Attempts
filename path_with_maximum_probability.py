#problem 1514: https://leetcode.com/problems/path-with-maximum-probability/

from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def dijkstra(src):
            pq = [(0,src)]
            dist[src] = 0
            visited = set()
            while pq:
                d, u = heappop(pq)
                if d > dist[u]: continue
                visited.add(u)
                for v, w in AH[u]:
                    if v in visited: continue
                    if u == src:
                        if dist[u] + w >= dist[v]: continue
                        dist[v] = dist[u] + w
                    else:
                        if -abs(dist[u] * w) >= dist[v]: continue
                        dist[v] = -abs(dist[u] * w)
                    heappush(pq, (dist[v], v))
        
        dist = n * [float("inf")]
        AH = defaultdict(list)
        for i in range(len(edges)):
            AH[edges[i][0]].append([edges[i][1],-succProb[i]])
            AH[edges[i][1]].append([edges[i][0],-succProb[i]])

        dijkstra(start)
        return abs(dist[end]) if abs(dist[end]) != float("inf") else 0
