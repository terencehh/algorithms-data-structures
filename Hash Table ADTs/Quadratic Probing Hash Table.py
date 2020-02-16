from referential_array import build_array


class Task4QuadraticHash:

    def __init__(self, key_value=31, size=27641):

        self.table_size = size
        self.array = build_array(self.table_size)
        self._count = 0
        self._total_probe = 0
        self._collisions = 0
        self._key_value = key_value
        self._max_load = (2/3)

    def __len__(self):
        return self._count

    def __iter__(self):
        return Task4QuadraticHash.Task4ListIterator(self)

    def get_key_value(self):
        return self._key_value

    def get_max_load(self):
        return self._max_load

    def get_total_probe(self):
        return self._total_probe

    def increment_count(self):
        self._count += 1

    def increment_probe(self):
        self._total_probe += 1

    def __str__(self):
        res = ""
        for i in range(self.table_size):

            if self.array[i] is not None:
                res = res + "(Key:" + str(self.array[i][0]) + " Item: " + str(self.array[i][1]) + ")"
                res += "\n"

        return res

    def increment_collisions(self):
        self._collisions += 1

    def get_collisions(self):
        return round(self._collisions, 2)

    def get_load(self):
        return round((len(self) / self.table_size), 2)

    def avg_probe_length(self):
        return round((self.get_total_probe() / len(self)), 2)

    def __getitem__(self, key):
        """
        :param self: hash table to search
        :param key: key of value to search
        :return: the value corresponding to key in the hash
                 table, if does not exist, KeyError raised
        :complexity: Worst-case: O(N) N for length of key
        :complexity: Best-case:  O(1) no item, can end early
        """

        position = self.hash_function(key)
        fixed_position = self.hash_function(key)  # value to store constant position
        counter = 0
        for _ in range(self.table_size):
            if self.array[position] is None:  # empty slot
                raise KeyError(key)
            elif self.array[position][0] == key:  # found it
                return self.array[position][1]
            else:
                # something there but different key
                # quadratic probing, so try next position
                counter += 1
                position = (fixed_position + (counter * counter)) % self.table_size

        raise KeyError(key)

    def make_dynamic(self):
        """
        :param self: hash table to search
        :return: null
        :complexity: Worst-case: O(N) Occurs N times for table size
        :complexity: Best-case:  O(N) Occurs N times for table size
        """
        new_size = ((self.table_size * 2) + 1)
        #  copy stuff to temp array
        #  set self array to larger array

        temp_array = self.array

        self.array = build_array(new_size)  # build array twice size +1
        self.table_size = new_size  # change current size variable into new one

        for i in range(len(temp_array)):  # rehash everything into larger array

            current_index = temp_array[i]

            if current_index is not None:  # found item to rehash

                # rehash key and store key and item into new larger array
                self[current_index[0]] = current_index[1]

    def __setitem__(self, key, value):
        """
        :param self: hash table to search
        :param key: key to undergo hash function to find the array position to set item
        :param value: value of data to insert
        :return: null
        :complexity: Worst-case: O(N) N for length of key
        :complexity: Best-case:  O(1) no item, can end early
        """
        counter = 0
        collision = False
        resized = False
        fixed_position = self.hash_function(key)  # value to store constant position
        position = self.hash_function(key)  # value to store position after quadratic probing

        for _ in range(self.table_size):

            if self.array[position] is None:  # found empty slot
                self.array[position] = (key, value)
                self.increment_count()

                if self.get_load() > self.get_max_load():
                    self.make_dynamic()
                    return

            elif self.array[position][0] == key:  # found key, replace value in key
                self.array[position] = (key, value)
                return
            else:  # not found, try next
                counter += 1
                position = (fixed_position + (counter * counter)) % self.table_size

                if not collision:
                    self.increment_collisions()
                    collision = True

                self.increment_probe()

        if not resized:  # quadratic probing did not find a array position to key in, so resize again
            self.make_dynamic()


    def __contains__(self, key):
        """
        :param self: hash table to search
        :param key: key to check if exist
        :return: True if exist, else False
        :complexity: Worst-case: O(N) Occurs N times for probe length
        :complexity: Best-case:  O(1) occurs when ends early
        """
        counter = 0
        fixed_position = self.hash_function(key)  # value to store constant position
        position = self.hash_function(key)  # value to store position after quadratic probing
        for _ in range(self.table_size):
            if self.array[position] is None:  # empty slot
                return False
            elif self.array[position][0] == key:  # found it
                return True
            else:
                counter += 1
                position = (fixed_position + (counter * counter)) % self.table_size
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


    class Task4ListIterator:

        def __init__(self, alist):
            self.array = alist.array
            self.current = 0
            self.high = len(alist)

        def __iter__(self):
            return self

        def __next__(self):
            if self.current == self.high:
                raise StopIteration
            else:
                item = self.array[self.current]
                self.current += 1
                return item


def main():
    pass
    


if __name__ == "__main__":
    main()

