# Sliding window

Dynamic sliding window have some shrink pattern  
### Run right until meet condition, shrink left to right to find optimize condition(Use for find min)  

**Pseudo code**
```plaintext
    left = 0, right = 0
    for right in range(n):
        while valid():
           left++
           #recalulate state
           ans = min(ans, right - left + 1)
```
**Problem list**
[209-minimum-size-subarray-sum.py](dynamic%2F209-minimum-size-subarray-sum.py)
[76-minimum-window-substring.py](dynamic%2F76-minimum-window-substring.py)


### While invalid(): shrink left to right until it valid again  (use for at most problem)
**Pseudo code**
```plaintext
    left = 0, right = 0
    for right in range(n):
        while invalid():
           left++
           #recalulate state
        #Now valid again, update result
        ans = max(ans, j - i + 1)
```
**Problem list**
[1838-frequency-of-the-most-frequent-element.py](dynamic%2F1838-frequency-of-the-most-frequent-element.py)
3. Longest Substring Without Repeating Characters
159. Longest Substring with At Most Two Distinct Characters (Medium)
340. Longest Substring with At Most K Distinct Characters
424. Longest Repeating Character Replacement
487. Max Consecutive Ones II
713. Subarray Product Less Than K
1004. Max Consecutive Ones III
1208. Get Equal Substrings Within Budget (Medium)
1493. Longest Subarray of 1's After Deleting One Element
1695. Maximum Erasure Value
1838. Frequency of the Most Frequent Element
2009. Minimum Number of Operations to Make Array Continuous
2024. Maximize the Confusion of an Exam
### Variant, find exact n = at most n  - at most n - 1  
[992-subarrays-with-k-different-integers.py](dynamic%2F992-subarrays-with-k-different-integers.py)
[1493-longest-subarray-of-1s-after-deleting-one-element.py](dynamic%2F1493-longest-subarray-of-1s-after-deleting-one-element.py)
[2062-count-vowel-substrings-of-a-string.py](dynamic%2F2062-count-vowel-substrings-of-a-string.py)
930. Binary Subarrays With Sum (Medium)
992. Subarrays with K Different Integers
1248. Count Number of Nice Subarrays (Medium)
2062. Count Vowel Substrings of a String (Easy)