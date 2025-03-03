import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operator = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operator:
                st.append(token)
            else:
                secondOperand = st.pop()
                firstOperand = st.pop()
                if token == "+":
                    currentResult = int(firstOperand) + int(secondOperand)
                elif token == "-":
                    currentResult = int(firstOperand) - int(secondOperand)
                elif token == "*":
                    currentResult = int(firstOperand) * int(secondOperand)
                else:
                    currentResult = math.trunc(int(firstOperand) / int(secondOperand))
                st.append(str(currentResult))
        return int(st[-1])
s = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(s))