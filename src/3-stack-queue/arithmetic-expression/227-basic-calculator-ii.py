import math
from collections import deque


class Solution:
    # def calculate(self, s: str) -> int:
    #     n = len(s)
    #     st = deque()
    #     operator = ['+', '-', '*', '/']
    #     i = 0
    #     currentNum = 0
    #     while i < n:
    #         if s[i] == ' ':
    #             i += 1
    #             continue
    #         if s[i] in operator:
    #             st.append(s[i])
    #         else:
    #             currentNum = currentNum * 10 + int(s[i])
    #             if i < n - 1 and s[i + 1].isdigit():
    #                 i += 1
    #                 continue
    #             if st and (st[-1] == '*' or st[-1] == '/'):
    #                 oper = st.pop()
    #                 firNum = st.pop()
    #                 if oper == '*':
    #                     curResult = firNum * currentNum
    #                 else:
    #                     curResult = math.trunc(firNum / currentNum)
    #                 st.append(curResult)
    #             else:
    #                 st.append(currentNum)
    #             currentNum = 0
    #         i += 1
    #     ans = st.popleft()
    #     while len(st) > 1:
    #         if '+' == st.popleft():
    #             ans += st.popleft()
    #         else:
    #             ans -= st.popleft()
    #     return ans
    def calculate(self, s: str) -> int:
        lastOperator = '+'
        currentNum = 0
        st = []

        for i in range(len(s)):
            if s[i].isdigit():
                currentNum = 10 * currentNum + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if lastOperator == '+':
                    st.append(currentNum)
                elif lastOperator == '-':
                    st.append(-currentNum)
                elif lastOperator == '*':
                    st.append(st.pop() * currentNum)
                else:
                    st.apapend(int(st.pop() / currentNum))
                lastOpeator = s[i]
                currentNumber = 0
        print(st)
        return sum(st)
s = "3+2*2"
print(Solution().calculate(s))