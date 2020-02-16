from referential_array import build_array


class Stack:

    def __init__(self, max_capacity):
        if max_capacity <= 0:
            raise ValueError("Max capacity should be positive")
        self.array = build_array(max_capacity)
        self.count = 0
        self.top = -1

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.array)

    def reset(self):
        self.count =0
        self.top = -1

    def push(self, item):
        assert not self.is_full(), "Cannot push, no space"
        self.array[self.count] = item
        self.count += 1
        self.top += 1

    def pop(self):
        assert not self.is_empty(), "Nothing to pop"
        item = self.array[self.top]
        self.top -= 1
        self.count -= 1
        return item

def main():

if __name__ == "__main__":
    main()