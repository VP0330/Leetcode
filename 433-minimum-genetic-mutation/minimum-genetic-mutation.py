class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bankset = set(bank)
        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            gene, mutation = queue.popleft()

            if gene == endGene:
                return mutation

            for i in range(len(gene)):
                for ch in "ACGT":
                    nei = gene[:i] + ch + gene[i+1:]

                    if nei in bankset and nei not in seen:
                        seen.add(nei)
                        queue.append((nei, mutation + 1))

        return -1