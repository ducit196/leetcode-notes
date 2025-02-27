
class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []
    def push(self, x: int) -> None:
        self.inputStack.append(x)

    def pop(self) -> int:
        self.consolidateOutput()
        return self.outputStack.pop()

    def consolidateOutput(self):
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())
    def peek(self) -> int:
        return self.outputStack[-1]

    def empty(self) -> bool:
        return not self.inputStack and not self.outputStack


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
param_3 = obj.peek()
param_4 = obj.empty()