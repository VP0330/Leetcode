from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen=set()
        seen.add(source)
        q=deque()
        q.append(source)
        while q:
            node=q.popleft()
            if node==destination:
                return True
            
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    q.append(neigh)
        return False
