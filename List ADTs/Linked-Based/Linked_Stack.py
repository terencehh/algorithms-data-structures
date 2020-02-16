from Node import Node

class LinkedStack:

    def __init__(self):
        self.top = None

    def is_full(self):
        return False

    def is_empty(self):
        return self.top is None

    def reset(self):
        self.top = None

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        assert not self.is_empty(), "Stack is empty"
        item = self.top.item
        self.top = self.top.next
        return item


def main():
    s = LinkedStack()
    s.push(5)
    s.push(2)
    s.push(6)
    s.push(3)
    s.push(1)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == "__main__":
    main()