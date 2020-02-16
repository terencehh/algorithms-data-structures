from referential_array import build_array


class LinearHash:

    def __init__(self, size=7919):
        self.count = 0
        self.table_size = size
        self.array = build_array(self.table_size)

    def __len__(self):
        return self.count

    def __str__(self):
        res = ""
        for i in range(self.table_size):

            if self.array[i] is not None:
                res = res + "(Key:" + self.array[i][0] + " Item: " + self.array[i][1] + ")"
                res += "\n"

        return res

    def __getitem__(self, key):
        """
        :param self: hash table to search
        :param key: key of value to search
        :return: the value corresponding to key in the hash
                 table, if does not exist, KeyError raised
        :complexity: Worst-case: O(N) N for length of key
        :complexity: Best-case:  O(1) no item, can end early
        """
        position = self.hash_value(key)
        for _ in range(self.table_size):
            if self.array[position] is None:  # empty slot
                raise KeyError(key)
            elif self.array[position][0] == key:  # found it
                return self.array[position][1]
            else:
                # something there but different key
                # linear probing, so try next position
                position = (position + 1) % self.table_size

        raise KeyError(key)

    def __setitem__(self, key, value):
        """
        :param self: hash table to search
        :param key: key to undergo hash function to find
                    the array position to set item
        :param value: value of data to insert
        :return: null
        :complexity: Worst-case: O(N) N for length of key
        :complexity: Best-case:  O(1) no collision, can end early
        """
        position = self.hash_value(key)
        for _ in range(self.table_size):
            if self.array[position] is None:  # found empty slot
                self.array[position] = (key, value)
                self.count += 1
                return
            elif self.array[position][0] == key:  # found key, replace value in key
                self.array[position] = (key, value)
                return
            else:  # not found, try next
                position = (position + 1) % self.table_size

        raise KeyError(key)  # key not found and hash table full

    def __contains__(self, key):
        """
        :param self: hash table to search
        :param key: key to check if exist
        :return: True if exist, else False
        :complexity: Worst-case: O(N) Occurs N times for probe length
        :complexity: Best-case:  O(1) No collision, can end early
        """
        position = self.hash_value(key)
        for _ in range(self.table_size):
            if self.array[position] is None:  # empty slot
                return False
            elif self.array[position][0] == key:  # found it
                return True
            else:
                position = (position + 1) % self.table_size
        return False

    def hash_value(self, key):
        """
        :param self: hash table to search
        :param key: input key to hash
        :return: the corresponding position in array of hash key result
        :complexity: Worst-case: O(N) loop for N length of key
        :complexity: Best-case:  O(N) loop for N length of key
        """
        a = 101
        h = 0
        for c in key:
            h = (h * a + ord(c)) % self.table_size
        return h


def main():
    test = LinearHash()
    test["apples"] = "Fuji"
    test["fun"] = "Cats"

    print(test["fun"])
    print(test["apples"])
    print("apples" in test)
    print(test)


if __name__ == "__main__":
    main()

