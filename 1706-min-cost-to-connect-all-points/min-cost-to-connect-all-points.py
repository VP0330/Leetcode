import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        seen=set()
        total_cost=0
        min_heap=[(0,0)]

        while len(seen)<n:
            dist,i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_cost+=dist
            xi,yi=points[i]

            for j in range(n):
                if j not in seen:
                   xj, yj = points[j]
                   nei_dis=abs(xi-xj)+abs(yi-yj)
                   heapq.heappush(min_heap,(nei_dis,j))
        return total_cost