from referential_array import build_array


class CircularQueue:

    def __init__(self, size):
        assert size > 0, "Size should be positive"
        self.array = build_array(size)
        self.count = 0
        self.rear = 0
        self.front = 0


    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.array)

    def reset(self):
        self.front = 0
        self.rear = 0
        self.count = 0

    def append(self, new_item):
        assert not self.is_full(), "Queue is full"
        self.array[self.rear] = new_item
        self.rear += 1
        if self.rear == len(self.array):
            self.rear = 0
        self.count += 1

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.array[self.front]
        self.front = (self.front+1) % len(self.array)
        self.count -= 1
        return item



def main():
    a = CircularQueue(5)
    a.append(5)
    a.append(3)
    a.append(1)
    a.append(7)
    a.append(9)
    print(a.serve())
    print(a.serve())
    print(a.serve())
    print(a.serve())
    print(a.serve())

if __name__ == "__main__":
    main()