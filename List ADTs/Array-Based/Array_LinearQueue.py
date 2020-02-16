from referential_array import build_array


class LinearQueue:

    def __init__(self, size):
        assert size > 0, "Size should be positive"
        self.array = build_array(size)
        self.count = 0
        self.rear = 0
        self.front = 0


    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.rear >= len(self.array)

    def reset(self):
        self.front = 0
        self.rear = 0
        self.count = 0

    def append(self, new_item):
        assert not self.is_full(), "Queue is full"
        self.array[self.rear] = new_item
        self.rear += 1
        self.count += 1

    def serve(self):
        assert not self.is_empty(), "Queue is empty"
        item = self.array[self.front]
        self.front += 1
        self.count -= 1
        return item


def main():
    a = LinearQueue(5)
    a.append(5)
    a.append(4)
    a.append(53)
    a.append(1)
    print(a.serve())
    print(a.serve())
    print(a.serve())
    print(a.serve())



if __name__ == "__main__":
    main()
