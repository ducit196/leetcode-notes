from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # move all exsting to new one
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        print(f'last = {self.q[-1]}')

        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

myStack =MyStack();
myStack.push(1);
myStack.push(2);
myStack.top() # return 2
myStack.pop() # return 2
myStack.empty() # return False