### Kadane algorithm

Very useful to find maximum sum of sub array  


Psuedo code
```plaintext
    
    for i in range(n):
        currentMaxSum = max(i, currentMaxSum + i)
        maxSum = max(maxSum, currentMaxSum
    return maxSum
```
###
Problem list    
1. Maximum Subarray (LeetCode #53)
2. Maximum Sum Circular Subarray (LeetCode #918)
3. Jump Game (LeetCode #55)
4. Jump Game II (LeetCode #45)(Kadane + greedy)
5. Best Time to Buy and Sell Stock(Kadane like)
6. Best Time to Buy and Sell Stock II
7. Longest Turbulent Subarray (LeetCode #978)
8.  Maximum Alternating Subarray Sum (LeetCode #1911)
9. Partition Array for Maximum Sum (LeetCode #1043)
10. Largest Sum of Averages (LeetCode #813)