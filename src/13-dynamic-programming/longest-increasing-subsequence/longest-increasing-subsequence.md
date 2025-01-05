# Longest increasing subsequence
Main idea of this problem is **connected to tail**  
At each element, loop from 0 -> i - 1, find max dp of all position that can be tail connected

### Pseudo code
```plaintext

    dp = [1] * n
    for i in range(n):
        for j in range(0, i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1  #check if can connected and find max dp
                dp[i] = dp[j] + 1

```