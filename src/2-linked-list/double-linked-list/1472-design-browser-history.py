class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next =next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        newNode = Node(url)     #create new node
        self.cur.next = newNode #point to new node
        newNode.prev = self.cur #new node point back
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            self.cur = self.cur.prev
        return self.cur.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            self.cur = self.cur.next
        return self.cur.val
obj = BrowserHistory("Home")
obj.visit("Page1")
print(obj.back(1))
print(obj.forward(1))