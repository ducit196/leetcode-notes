
class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

    def add(self, num: int) -> None:
        if num == 0: #reser
            self.product = [1]
        else:
            self.product.append(self.product[-1] * num)


    def getProduct(self, k: int) -> int:
        if len(self.product) - 1 < k:
            return 0
        return self.product[-1] // self.product[len(self.product) - 1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
# print(obj.getProduct(2))
# print(obj.getProduct(3))
print(obj.getProduct(3))