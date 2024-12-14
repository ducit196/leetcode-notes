# Union Find
Implement a class to represent and undirected graph:  
* MyGraph(int n): initiate a graph, n vertex and no edges
* add(u, v) --> add an edge u, v
* boolean query(u, v) --> check if u and v are connected?
* int count(): number of connected components?
![img.png](img.png)
In this case, graph is dynamic, BFS and DFS are very complexity. Best case of DFS/BFS is static graph  
**Union Find algorithm**  
Statement 1: 2 vertex are connected --> has same root  
Statement 2: if we add an edge(u, v) --> we can say edge(root of u, root of v)  
There are 2 function
union(u, v) --> union component of u and v
find(u) --> root of u  
Pseudo code  
```plaintext
    parent = [-1] * n
    def find(u: int) ->int: #find root of u
        while parent[u] != -1:
            u = parent[u]
        return u
    
    def union(int u, int v):    #union 2 connected component
        parent[v] = u
    
    def add(int i, int j):
        #find root i and j
        u = find(i)
        v = find(j)
        if u != v:  #if root of u and root of v are different --> union
            union(u,v)
            
    def query(int i, int j):
        return find(i) == find(j) --> root of i == root of j --> connected component
```