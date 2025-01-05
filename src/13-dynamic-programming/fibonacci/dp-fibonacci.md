# DP Fibonacci pattern
Sign: same as fibonacci, either we start with step 1 or step 2
Recursive: dp[i] = dp[i - 1] + dp[i - 2]
### Pseudo code
Top down
```plaintext
    def dp(i):
        #Base case:
        if i == 0, 1:
            return base element.
        return dp[i - 1] + dp[i - 2]
```
Bottom up  
```plaintext
    dp[] = [0] * n + 1
    dp[0] = 0, dp[1] = 1 #assign base element
    for i in range(2, n + 1)
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]
    
```
DP with save memory
```plaintext
      
    prev2 = 0, prev = 1, current = 0 #assign base element
    for i in range(2, n + 1)
        current = prev + prev2 #cal current dp
        prev2 = prev
        prev = current
    return current
    
```
    