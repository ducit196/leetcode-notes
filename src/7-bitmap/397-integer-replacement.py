from itertools import count


class Solution:
    def integerReplacement(self, n: int) -> int:
        #Idea: In case of odd, between n - 1 and n + 1, Choose solution that can be % 2 == 0. 1 edge case, if n == 3 choose n - 1
        # TC: O(log(n)
        # SC: O(1)
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            elif ((n - 1) / 2) % 2 == 0 or ((n - 1) / 2) == 1:
                n = n - 1
            else:
                n = n + 1
            count += 1
        return count
print(Solution().integerReplacement(3))