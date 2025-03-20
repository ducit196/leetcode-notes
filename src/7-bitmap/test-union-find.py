from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Union-Find with path compression and rank
        parent = list(range(n))
        rank = [1] * n  # To optimize union by rank

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])  # Path compression
            return parent[u]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU != rootV:
                # Union by rank
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1

        # Step 1: Build Union-Find
        for u, v, _ in edges:
            union(u, v)

        # Step 2: Process Queries
        ans = []
        for u, v in query:
            if find(u) == find(v):
                ans.append(0)  # If they are connected, return 0 (modify as needed)
            else:
                ans.append(-1)  # Otherwise, they are in different components

        return ans


# Example usage
n = 5
edges = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
query = [[1, 3], [3, 4]]
print(Solution().minimumCost(n, edges, query))
