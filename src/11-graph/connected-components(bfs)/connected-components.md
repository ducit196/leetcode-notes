# Count number of connected components(2D Matrix)

Sample problem 200: number of islands  

```plaintext
    grid = [1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1]
A connected component is number of edges can connect adjiacent(4 directions or 8 directions)  
Traverse all land cell(grid[i][j] == 1)  
    At each cell, DFS or BFS to traverse remaining cell in componants
    Once finished DFS or BFS --> increase 1 componant
```
Pseudo code  
```plaintext
    ans = 0
    for i in m:
        for j in n:
            if (i,j) is a land and not in visited
                ans++
                bfs(i,j)
```