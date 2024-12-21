# Floyed Warshall
Find minimum path between all vertices  
Precondition: there is **no negative cyclic**

### Pseudo code
```plaintext
   #Initiate weight edge matrix, no edge -> weight = 'inf'
   for k in range(n):
       for i in range(n):
            for j in range(n):
                if d[i][j] < d[i][k] + d[k][j]
                    d[i][j] = d[i][k] + d[k][j]
   --> matrix d is minimum path bettwen all vertices
```
