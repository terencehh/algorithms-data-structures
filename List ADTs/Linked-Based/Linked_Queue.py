from Node import Node

class LinkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        #self.count = 0

    def is_full(self):
        return False

    def is_empty(self):
        return self.front is None

    def __len__(self):
        return self.count

    def serve(self):
        assert not self.is_empty(), "The queue is empty"
        temp = self.front.item
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        return temp

    def append(self, item):
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

def main():
    q = LinkedQueue()
    q.append(5)
    q.append(2)
    q.append(6)
    q.append(3)
    q.append(1)
    print(q.serve())
    print(q.serve())
    print(q.serve())
    print(q.serve())
    print(q.serve())


if __name__ == "__main__":
    main()