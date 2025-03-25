from collections import deque
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #edges list to adj
        adjList = [[] for i in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = set()
        #Each node, try to explore all adj and add to component
        #after visit, check if number of edge from each node, should be match with number of node component - 1
        #Sample a square, has 4 vertex. Each vertext have to connect with 4 - 1 remaining vertex
        ans = 0
        for i in range(n):
            if i not in visited:
                component = []
                component.append(i)
                visited.add(i)
                q = deque()
                q.append(i)

                while q:
                    currentNode = q.popleft()
                    for neighbor in adjList[currentNode]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            component.append(neighbor)
                            q.append(neighbor)
                #check if component valid
                validComponent = 1
                for c in component:
                    if len(adjList[c]) != len(component) - 1:
                        validComponent = 0
                        break
                ans += validComponent
        return ans
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
print(Solution().countCompleteComponents(n, edges))