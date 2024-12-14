# Path finding
In path finding problem, I mostly use BFS and DFS to traverse the graph and keep track the path
### DFS template
```plaintext
def dfs(node, visited)
    if node in visited:
        return
    Mark node as visited
    process(node) # Do something as require: add path, print,...
    for neighbor in neighbors of node:
        dfs(neighbor, visited)
```
### BFS template
```plaintext
def bfs(node): #start node
    queue.enqueue(node)
    while queue not empty:
        currentNode = queue.dequeue()
        if node is not visited:
            Visist currentNode
            process(currentNode) # Do something as require: add path, print,...
            if neighbor is not in visited:
                queue.enqueu(neighbor) #Add to the queue
```