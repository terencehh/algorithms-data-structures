from referential_array import build_array


class List:

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


    def add(self, new_item):
        has_space_left = not self.is_full()
        if has_space_left:
            self.array[self.count] = new_item
            self.count += 1
        return has_space_left

    def delete(self, index):
        valid_index = index >= 0 and index < self.count
        if valid_index:
            for i in range(index, self.count-1):
                self.array[i] = self.array[i+1]
            self.count -= 1
        return valid_index

    def __str__(self):
        ans = "["
        for i in range(self.count):
            ans += str(self.array[i])
            ans += ","
        ans += ']'
        return ans


def main():

    a_list = List(4)
    a_list.add(4)
    a_list.add(3)
    a_list.add(1)
    a_list.add(10)
    a_list.delete(1)
    print(str(a_list))




if __name__ == "__main__":
    main()

