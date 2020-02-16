from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def __str__(self):
        """
        :param self: list object
        :return: a string containing all items in the list
        :complexity: Worst-case: O(N) for when node != None
        :complexity: Best-case: O(1) for when node == None
        """
        ans = ""
        node = self.head
        while node is not None:
            ans += str(node.item)
            node = node.next
            ans += "\n"
        return ans

    def __len__(self):
        """
        :param self: list object
        :return: length of list
        :complexity: Worst-case: O(1)
        :complexity: Best-case: O(1)
        """
        return self.count

    def __getitem__(self, index):
        """
        :param self: list object
        :param index: integer stating list item position
        :return: item based on list index
        :complexity: Worst-case: O(N) for N index
        :complexity: Best-case: O(1) when index out of range or index == 0
        """
        if not(-len(self)) <= index < len(self):
            raise IndexError("Index out of range")
        else:
            node = self.head
            if index == 0:
                return node.item
            elif index > 0:
                for _ in range(index):
                    node = node.next
                return node.item
            else:
                start = self.count + index
                for _ in range(start):
                    node = node.next
                return node.item

    def __setitem__(self, index, item):
        """
        :param self: list object
        :param index: integer stating list item position
        :param item: integer stating list item
        :return: Null
        :complexity: Worst-case: O(N) for N index
        :complexity: Best-case: O(1) when index out of range or index == 0
        """
        if not(-len(self)) <= index < len(self):
            raise IndexError("Index out of range")
        else:
            node = self.head
            if index == 0:
                node.item = item
            elif index > 0:
                for _ in range(index):
                    node = node.next
                node.item = item
            else:
                start = self.count + index
                for _ in range(start):
                    node = node.next
                node.item = item

    def __contains__(self, item):
        """
        :param self: list object
        :param item: integer stating list item
        :return: True or False if item in list
        :complexity: Worst-case: O(N) for N when current != None
        :complexity: Best-case: O(1) if current is None
        """
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False

    def __eq__(self, other):
        """
        :param self: list object
        :param other: python list object or ADT list
        :return: True or False depending on if self == other
        :complexity: Worst-case: O(N) occur (N) times for current != None
        :complexity: Best-case: O(1) occur when length of list is not equal
        """
        if len(self) == len(other):
            current = self.head
            counter = 0
            while current is not None:
                if not current.item == other[counter]:
                    return False
                else:
                    current = current.next
                    counter += 1
            return True
        else:
            return False

    def append(self, item):
        """
        :param self: list object
        :param item: integer stating list item
        :return: Null
        :pre-condition: item is a valid integer or string
        :post-condition: altered list with item inserted end of list
        :complexity: Worst-case: O(N) N for while current is not None
        :complexity: Best-case: O(1) occur when current == None or current.next == None
        """
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = (Node(item, None))

        else:
            self.head = Node(item, None)

        self.count += 1

    def insert(self, index, item):
        """
        :param self: list object
        :param index: integer stating list item position
        :param item: integer stating list item
        :return: Null
        :pre-condition: index is a valid position in list, list is not full
        :post-condition: altered list with item inserted into index
        :complexity: Worst-case: O(N) loops for N times
        :complexity: Best-case: O(1)  occur if index out of range or index == 0 or -len(self)
        """
        if not (-len(self)) <= index <= len(self):
            raise IndexError("Index out of range")

        if index == 0 or index == -len(self):
            self.head = Node(item, self.head)

        elif index > 0:
            current = self.head
            # get current item index
            for i in range(index-1):
                current = current.next
            current.next = Node(item, current.next)

        elif index < 0:
            current = self.head
            # get current item index
            for i in range(self.count + index - 1):
                current = current.next

            current.next = Node(item, current.next)

        self.count += 1

    def remove(self, item):
        """
        :param self: list object
        :param item: integer stating list item
        :return: Null
        :pre-condition: item is a valid integer or string
        :post-condition: altered list with index item removed or ValueError
        :complexity: Worst-case: O(N) Occur N times for when current != None
        :complexity: Best-case: O(1) Occur when head is the item
        """
        current = self.head
        if current.item == item:
            self.head = current.next
        else:
            while current is not None:

                if current.next is None:
                    raise ValueError("Item does not exist")
                elif current.next.item == item:
                    current.next = current.next.next
                    break
                else:
                    current = current.next

        self.count -= 1

    def delete(self, index):
        """
        :param self: list object
        :param index: integer stating list item position
        :return: Null
        :pre-condition: index is a valid position in list
        :post-condition: altered list with index item removed
        :complexity: Worst-case: O(N) #only one comparision on each pass
        :complexity: Best-case: O(1) Occur when index out of range or index == 0 or -len(self)
        """
        if not (-len(self)) <= index < len(self):
            raise IndexError("Index out of range")

        if index == 0 or index == -len(self):
            self.head = self.head.next
            self.count -= 1

        elif index > 0:
            current = self.head  # get current item index - 1
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
            self.count -= 1

        elif index < 0:
            current = self.head  # get current item index - 1
            for i in range(self.count + index - 1):
                current = current.next
            current.next = current.next.next
            self.count -= 1

    def sort(self, reverse):
        """
        :param self: list object to be performed on
        :param reverse: tells condition
        :return: Null
        :pre-condition: all integer elements for list
        :post-condition: list sorted ascending or descending
        :complexity: Worst-case: O(N^2) N comparisons inside N-1 times loop for index
        :complexity: Best-case: O(N) loop N-1 times for index, list is already sorted
        """
        if reverse:
            for index in range(1, self.count):
                current_value = self[index]
                position = index
                while position > 0 and self[position - 1] < current_value:
                    self[position] = self[position - 1]
                    position = position - 1

                self[position] = current_value
        else:
            for index in range(1, self.count):
                current_value = self[index]
                position = index
                while position > 0 and self[position - 1] > current_value:
                    self[position] = self[position - 1]
                    position = position - 1
                self[position] = current_value


class ListIterator:

    def __init__(self, alist):

        self.current = alist.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item_required = self.current.item
            self.current = self.current.next
            return item_required


def main():
    a_list = LinkedList()
    a_list.insert(1,1)
    a_list.append(2)

    #a_list.insert(1, "x")
    print(a_list)



if __name__ == "__main__":
    main()

