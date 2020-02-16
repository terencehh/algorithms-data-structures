from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return False

    def reset(self):
        self.__init__()

    def _get_node(self, index):
        if not(-len(self)) <= index < len(self):
            raise IndexError("Index out of range")
        else:
            if index > 0:
                node = self.head
                for _ in range(index):
                    node = node.next
                return node
            else:
                node = self.head
                start = self.count + index
                for _ in range(start, index):
                    node = node.next
                print(node)
                return node

    def insert(self, index, item):
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)
        if index == 0:
            self.head = Node(item, self.head)
        else:
            curnode = self._get_node(index-1)
            curnode.next = Node(item, curnode.next)

        self.count += 1

    def delete(self, index):
        if self.is_empty():
            raise IndexError("The list is empty")
        if index < 0 or index >= len(self):
            raise IndexError("Index is out of range")
        if index == 0:
            self.head = self.head.next
        else:
            node = self._get_node(index-1)
            node.next = node.next.next
        self.count -= 1
    
    def __str__(self):
        ans = ""
        node = self.head
        while node is not None:
            ans += str(node.item)
            node = node.next
            ans += "\n"
        return ans

    # Two pointer Approach. Floyd's Cycle Detection Algorithm
    def check_cycle(self):

        if(self.head == None):
            return False

        tortoise = self.head
        hare = self.head
        while(hare.next != None and hare.next.next != None):
            tortoise = tortoise.next
            hare = hare.next.next
            if(hare == tortoise):
                return True
        return False


def main():
    a = LinkedList()
    a.insert(0, 5)
    a.insert(1, 7)
    a.insert(2, 9)
    print(a.check_cycle())

    print(a)


if __name__ == "__main__":
    main()