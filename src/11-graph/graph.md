# Graph

### Concept



### Code simulator
There are 3 popular type of graph simulator

* Adjacency matrix
* Adjacency matrix
* Edge list



### Topic

#### [Path finding](path-finding/path-finding.md)
Find path from source to target.  
**Idea**: DFS and BFS  
**Problem list:**  
797 - [All Paths From Source to Target](path-finding/797-all-path-source-target-bfs.py)  
1091 - [Shortest Path in Binary Matrix](path-finding/1091-shortest-path-binary-matrix.py)
#### [Bipartite(Coloring)](bipartite/bipartite.md)
Bipartite graph is a graph that we can divide edges into 2 separate groups.  
Each group there is no connection between them.  
**Idea**: 2 adjacent vertices color 2 opposite color, do the same for all, if can see any conflict --> return false  
**Problem list:**  
[785](https://leetcode.com/problems/is-graph-bipartite/) - [Is bipartite graph](bipartite/785-is-bipartite-graph.py)  
[886](https://leetcode.com/problems/possible-bipartition/description/) - [Possible Bipartite](bipartite/886-possible-bipartition.py)
#### [Connected components 2D maxtrix](connected-components(bfs)/connected-components.md)
**Problem list:**  
200 - [Number of islands](connected-components(bfs)/200-number-of-island.py)  
695 - [Max area of islands](connected-components(bfs)/695-max-area-off-island-dfs.py) Similar to number of island, just count and find max  
130 - [Surrounded regions](connected-components(bfs)/130-surrounded-regions.py)

#### [Union Find](union-find/union-find.md)
Resolve problem related group data, find connected component, cycle detection, dynamic added edge in graph
**Idea**: 2 vertices are connected --> same root. 
#### [Topological sort](topological-sort/topological-sort.md)
To resolve pre require problem. Sample pre require learning course  
**Idea**: if any vertices has degree = 0 --> study and remove
**Problem list:**  
207 - [Course schedule](topological-sort/207-course-schedule.py)  
210 - [Course schedule 2](topological-sort/210-course-schedule-2.py)  
1462 - [Course schedule 4](topological-sort/1462-course-schedule-4.py)  
2192 - [All ancestors of a node](topological-sort/2192-all-ancestors-of-a-node.py)

[#### Floyed Warshall](weighted-graph/floy-washall/floyed-warshall.md)  
Find min path between all vertices in a graph has **no negative cyclic**. TC: = O(n3)  
**Idea**: there is a intermediate point k. If a[i][j] < a[i][k] + a[j][j] --> a[i][j] = a[i][k] + a[k][j] --> Find better solution

#### [Dijkstra](weighted-graph/dijkstra/dijkstra.md)
Find min path from 1 vertex to other vertices(no negative weight)  
**Idea:**: At every moment, select best solution. Put all neighbor in to a min heap to make sure best solution will be selected first  
