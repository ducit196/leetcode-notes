# DP with backtracking + bitmasking
Find all possible case

```plaintext
    def choose(iw, usedBike):       #usedBike use for tracking used items
        if iw == n:
            return 0
        ans = math.inf
        for b in rangen(bikes):
            if usedBike >> b & 1 == 1
                continue
            newUsedBike = usedBike | 1 << b #mark that bike bth is used
            ans = min(ans, choose(iw + 1, newUsedBike) + distance of ith)
        return ans
```