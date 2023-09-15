import heapq

class Solution:
    def minCostConnectPoints(self, points):
        
        n = len(points)
        min_cost = 0
        visited = [False] * n
        pc = [(0, 0)]
        cache = {0: 0}
        while pc:
            cost, vertex = heapq.heappop(pc)

            if visited[vertex]:
                continue

            visited[vertex] = True
            min_cost += cost

            for p in range(n):
                if not visited[p]:
                    distance = abs(points[vertex][0] - points[p][0]) + abs(points[vertex][1] - points[p][1])

                    if distance < cache.get(p, distance + 1):
                        cache[p] = distance
                        heapq.heappush(pc, (distance, p))

        return min_cost