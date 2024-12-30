# Dynamic programming
### Concept
Dynamic programming, try all possibility case but memory previous step result  
#### Top down
When to use:  
We don't need to resolve thoroughly sub problem(coin change)

Recursive + memo  
Sample fibonacci
```plaintext
    memo = {}
    def fib(n):
        if n < 2:
            return n
        if n in memo:   #Memo sub problem so don't need calculate again
            return n
        else:
            memo[n] = fib(n - 1) + fib(n -2 )
            return memo[n]
    
```
#### Bottom up(Tabulation)
From bottom, build the result up to top
```plaintext
    def fib(n):
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n):
            dp[i] = d[i - 1] + dp[i - 2]
        return dp[n]
```


