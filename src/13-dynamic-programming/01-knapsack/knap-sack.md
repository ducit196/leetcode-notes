# Knap sack problem
This problem normally we take or no take current index, then find max, min  
Normally use 2 variable (index, currentResult) for top down or use 2D tabulation 

### Pseudo code
Top down
```plaintext
    def dp(i, w):
        #Base case:
        if i == 0:
            return 0
        skip = dp(i - 1, w) #skip to next item, w remaining same
        take = dp(i - 1, w + nums[i] #take this item, increase w and move to next items
        return max(skip, take)
```
    