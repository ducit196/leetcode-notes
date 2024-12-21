# Dijkstra
This algorithm use to find minimum path from a vertex for other vertices  
Precondition: graph **without** negative weight

### Pseudo code  
    
```plaintext
    heap.push(du, 0) #starting point
    d[0] = 0 #d = minimum path from starting point
    while heap:
        du, u = heappop(heap)
        if u in fixed:
            continue
        fixed.add(u)
        for neighbor in adjList[u]:
            if neighbor not in fixed and d[u] + weight[u][neightbor] < d[neighbor]
                d[neightborr] = d[u] + weight[u][neightbor]
                heap.push(d[neightbor], neighbor)
        --> d is minimum from starting point to other
```

Probplem list  

787. Cheapest Flights Within K Stops
778. Swim in Rising Water
815. Bus Routes
1091. Shortest Path in Binary Matrix
1631. Path With Minimum Effort
2812. Find the Safest Path in a Grid
2642. Design Graph With Shortest Path Calculator