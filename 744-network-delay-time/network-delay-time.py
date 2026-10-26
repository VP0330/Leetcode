class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=defaultdict(list)

        for u,v,time in times:
            graph[u].append((v,time))
        
        min_time={}
        min_heap=[(0,k)]

        while min_heap:
            source_to_i, i = heapq.heappop(min_heap)

            if i in min_time:
                continue
            
            min_time[i]=source_to_i 
            for neigh, neigh_times in graph[i]:
                if neigh not in min_time:
                    heapq.heappush(min_heap,(source_to_i+neigh_times,neigh))
        if len(min_time)==n:
            return max(min_time.values())
        else:
                return -1

            
        