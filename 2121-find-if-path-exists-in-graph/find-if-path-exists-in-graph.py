class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        if source == destination:
            return True
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen=set()
        seen.add(source)
        q=deque()
        q.append(source)

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    q.append(neigh)
        return False