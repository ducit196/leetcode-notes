class StockSpanner:

    def __init__(self):
        self.monoStack = []

    def next(self, price: int) -> int:
        span = 0
        while self.monoStack and price >= self.monoStack[-1][0]:
            indexPrice, indexSpan = self.monoStack.pop()
            span += indexSpan
        self.monoStack.append((price, span + 1))
        return span + 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)