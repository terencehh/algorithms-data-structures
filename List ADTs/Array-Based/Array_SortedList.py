from referential_array import build_array


class SortedList:

    def __init__(self, max_capacity):
        if max_capacity <= 0:
            raise ValueError("Size should be positive")
        self.count = 0
        self.array = build_array(max_capacity)

    def __len__(self):
        return self.count

    def is_empty(self):
        return len(self) == 0

    def is_full(self):
        return len(self) >= len(self.array)

    def index(self, item):
        if self.is_empty():
            return "Empty List"
        low = 0
        high = len(self.array)-1
        mid = low + high // 2

        while True:
            if self.array[mid] == item:
                return mid
            else:
                if item < self.array[mid]:
                    high = mid - 1
                    mid = low + high // 2
                else:
                    low = mid + 1
                    mid = low + high // 2

    def add(self, item):
        has_space_left = not self.is_full()
        if has_space_left:
            #figure out position of new item
            position = 0
            for i in range(self.count):
                if self.array[i] < item:
                    position += 1
                else:
                    break
            #position is the place where new item goes
            for i in range(self.count - 1, position - 1, -1):
                #move item in position i to i+1
                self.array[i+1] = self.array[i]
            #add new item
            self.array[position] = item
            self.count += 1
        return has_space_left

    def __str__(self):
        ans = "["
        for i in range(self.count):
            ans += str(self.array[i])
            ans += ","
        ans += ']'
        return ans


def main():

    a_list = SortedList(4)
    a_list.add(4)
    a_list.add(3)
    a_list.add(1)
    a_list.add(10)
    print(str(a_list))
    print(a_list.index(10))
    print(a_list.index(3))


if __name__ == "__main__":
    main()

