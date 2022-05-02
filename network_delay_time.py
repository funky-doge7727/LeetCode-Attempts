from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(s):
            pq = [(0,s)]
            dist[s] = 0
            while pq:
                d, u = heappop(pq)
                if d > dist[u]: continue
                for v, w in AL[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heappush(pq, (dist[v], v))

        AL = [[] for _ in range(n+1)] # 1-based
        AL[0] = None

        for u, v, w in times:
            AL[u].append((v, w))

        dist = [float("inf")] * (n+1)
        dist[0] = -1

        dijkstra(k)
        maxx = max(dist)
        return maxx if maxx != float("inf") else -1
