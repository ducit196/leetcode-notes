# Array

## Two Pointer
Use to reduce time complexity from O(n2) to O(n)  
There are 2 types:  
### Fast and slow tow pointer  
[283-move-rezoes.py](two-pointer%2Fslow-fast%2F283-move-rezoes.py)  
[26-remove-duplicate-from-sorted-array.py](two-pointer%2Fslow-fast%2F26-remove-duplicate-from-sorted-array.py)
### Two pointer start from both end  
Normally, start from both end then shrink base on greedy or any optimize condition  
[11-container-most-water.py](two-pointer%2Fstart-end%2F11-container-most-water.py)  
[125-valid-palidrome.py](two-pointer%2Fstart-end%2F125-valid-palidrome.py)  
[189-rotate-array.py](two-pointer%2Fstart-end%2F189-rotate-array.py)

## Sliding Window
There are 2 type, static and dynamic sliding window  
**Static**: calculate first window, one by one moving window then compare with target  
[438-find-all-anagrams-string.py](sliding-window%2Fstatic%2F438-find-all-anagrams-string.py)  
**Dynamic**: Run right pointer until meet the condition, shrink left to right to check if we still meet expectation --> Find min, max  
[3-longest-substring-without-repeating-characters.py](sliding-window%2Fdynamic%2F3-longest-substring-without-repeating-characters.py)  
[76-minimum-window-substring.py](sliding-window%2Fdynamic%2F76-minimum-window-substring.py)  
[209-minimum-size-subarray-sum.py](sliding-window%2Fdynamic%2F209-minimum-size-subarray-sum.py)  

## Prefix Sum
Precompute sum of array, then can quick cal sum of range number  
Reduce time complexity from O(n2) to O(n)  
**Pseudo code**  
```plaintext
    for i in range(n):
        preSum[i + 1] = preSum[i] + num[i]
    ---> sum(i, j) = preSum[j + 1] - preSum[i]
```
[304-range-sum-query-2d.py](prefix-sum%2F304-range-sum-query-2d.py)  
[525-contigous-array.py](prefix-sum%2F525-contigous-array.py)  
[1422-max-score-afters-split-string.py](prefix-sum%2F1422-max-score-afters-split-string.py)  
[1769-minimum-operation-move-all-ball-to-each-box.py](prefix-sum%2F1769-minimum-operation-move-all-ball-to-each-box.py)  
[2270-number-ways-split-array.py](prefix-sum%2F2270-number-ways-split-array.py)  
[2381-Shifting-Letters-II.py](prefix-sum%2F2381-Shifting-Letters-II.py)  
[2559-count-vowel-strings-in-range.py](prefix-sum%2F2559-count-vowel-strings-in-range.py)  

## 2D Matrix
## Partition amd Segregation
## Rotate and Reverse