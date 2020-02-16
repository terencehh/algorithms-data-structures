class ListIterator:

    def __init__(self, head):
        self.current = self.array[head]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item_required = self.current
            head += 1
            self.current = self.array[head]
            return item_required
