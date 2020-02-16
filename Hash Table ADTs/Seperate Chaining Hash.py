from LinkedList import LinkedList
from task2 import *


class SeparateChainingHash:

    def __init__(self, key_value=31, size=7919):
        self._count = 0
        self._total_probe = 0
        self._collisions = 0
        self._key_value = key_value

        self.table_size = size
        self.array = [LinkedList() for _ in range(self.table_size)]

    def __len__(self):
        return self._count

    def increment_collisions(self):
        self._collisions += 1

    def get_collisions(self):
        return round(self._collisions, 2)

    def get_load(self):
        return round((self._count / self.table_size), 2)

    def avg_probe_length(self):
        return round((self.get_total_probe() / self._count), 2)

    def get_key_value(self):
        return self._key_value

    def get_total_probe(self):
        return self._total_probe

    def increment_count(self):
        self._count += 1

    def increment_probe(self):
        self._total_probe += 1

    def __str__(self):
        res = ""
        for i in range(self.table_size):

            for j in range(len(self.array[i])):

                res = res + "Key: " + self.array[i][j][0] + " Item: " + self.array[i][j][1] + ""
                res += "\n"

        return res

    def __getitem__(self, key):
        """
        :param self: hash table to search
        :param key: key of value to search
        :return: the value corresponding to key in the hash
                 table, if does not exist, KeyError raised
        :complexity: Worst-case: O(N) Occurs N times for probe length
        :complexity: Best-case:  O(1) no collision, can end early
        """
        position = self.hash_function(key)

        for i in self.array[position]:
            if key in i:
                return i[1]  # found it

        raise KeyError(key)  # key not found and hash table full

    def __setitem__(self, key, value):
        """
        :param self: hash table to search
        :param key: key to undergo hash function to find
                    the array position to set item
        :param value: value of data to insert
        :return: null
        :complexity: Worst-case: O(N) Occurs N times for probe length
        :complexity: Best-case:  O(1) No collision, can end early
        """
        collision = False
        position = self.hash_function(key)

        if len(self.array[position]) == 0:  # empty, no collisions or probe
            self.array[position].append((key, value))
            self.increment_count()
            return

        # if already have elements at hash index

        for i in range(len(self.array[position])):

            if self.array[position][i][0] == key:  # found key, replace value in key
                self.array[position][i] = (key, value)
                return

            else:
                if not collision:
                    self.increment_collisions()
                    collision = True

                self.increment_probe()

        self.array[position].append((key, value))  # add key after probing length of linked list
        self.increment_count()

    def __contains__(self, key):
        """
        :param self: hash table to search
        :param key: key to check if exist
        :return: True if exist, else False
        :complexity: Worst-case: O(N) Occurs N times for probe length
        :complexity: Best-case:  O(1) No collision, can end early
        """
        position = self.hash_function(key)
        for i in self.array[position]:
            if key in i:
                return True

        return False

    def hash_function(self, key):
        """
        :param self: hash table to search
        :param key: input key to hash
        :return: the corresponding position in array of hash key result
        :complexity: Worst-case: O(N) loop for N length of key
        :complexity: Best-case:  O(N) loop for N length of key
        """
        value = self.get_key_value()
        h = 0
        for c in key:
            h = (h * value + ord(c)) % self.table_size
        return h


def main():
    size_values = [210000, 209987, 400000, 399989, 202361]
    files = ["english_small.txt", "english_large.txt", "french.txt"]
    hash_constant = [15, 77, 48, 181, 271]

    task5_time_taken(files, size_values, hash_constant)


if __name__ == "__main__":
    main()

