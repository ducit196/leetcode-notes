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
### Pattern
#### [Fibonacci](fibonacci/dp-fibonacci.md)  
62 Unique path  
63 Unique path 2  
70 Climbing stair  
91 Decode ways  
198 House robber
213 house robber 2
Number factors  
Minimum jumps to reach the end  
Minimum jumps with fee  
House thief  
Staircase  
#### [0/1 Knapsack](01-knapsack/knap-sack.md)  
Subset Sum  
Equal Sum Partition  
Count of subset with given sum  
Minimum subset sum difference  
Target Sum  
No of susbet with given difference  
Count of subsets with given difference  
Last Stone Weight 2(LC 1049)  
#### [Longest common subsequence](longest-common-subsequence/longest-common-subsequence.md)  
Longest Common Substring  
Print LCS  
Shortest Common Supersequence  
Print SCS  
Minimum number of insertions and deletions to from String a from String b  
Largest Repeating Subsequence  
Length of largest subsequence of which is a substring in b  
Subsequence Pattern Matching  
Count number of times a appear as subsequence in b  
Largest Pallindromic Subsequence  
Longest Pallindromic Substring  
Count of Pallindromic Substring  
Minimum deletions to make a string Pallindrome  
Minimum insertions to make a string Pallindrome  
Minimum deletions to make a->b  

#### [Longest increasing subsequence](longest-increasing-subsequence/longest-increasing-subsequence.md)  
Maximum Sum Increasing Subsequence  
Print LIS  
Best Team with No Conflicts (LC 1626)  
No of LIS  
Increasing Triplet Subsequence  
LIS having sum almost K  
Minimum Number of Removals to Make Mountain Array

#### [DP + Backtracking + Bitmap](dp-backtracking/dp-backtracking.md)  
1006 campus bike  
1799 Maximize score after n operations  
2376 count special integer  
#### [Classic DP](classic/classic-dp.md)  

#### Kadane's Algo:(Need learn)

Maximum difference of 0's and 1's in a binary string  
Maximum Sum Circular array  
Smallest sum contiguous subarray  
Largest sum increasing contiguous subarray  
Maximum Product Subarray  
Largest sum contiguous subarray with only non-negative elements.  
Largest sum contiguous subarray with unique elements.  
Maximum Alternating Sum Subarray  
Maximum Sum Rectangle In A 2D Matrix  

#### Matrix Chain Multiplication(Need learn)
Priting MCM  
Burst Ballons  
Evaluate Expression to True/ Boolean Paranthesization  
Minimum / Maximum Value of an Expression  
Pallindrome Partitioning  
Scramble String  
Egg Dropping Problem  