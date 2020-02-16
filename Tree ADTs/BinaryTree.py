from TreeNode import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, item, positionbitstring):
        bitstring_iterator = iter(positionbitstring)
        self.root = self._add_aux(self.root, item, bitstring_iterator)

    def __len__(self):
        return self.len_aux(self.root)

    def len_aux(self, current):
        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def get_leaves(self):
        a_list = []
        self.get_leaves_aux(self.root, a_list)
        return a_list

    def get_leaves_aux(self, current, a_list):
        if current is not None:
            if self.is_leaf(current):
                a_list.append(current.item)
            else:
                self.get_leaves_aux(current.left, a_list)
                self.get_leaves_aux(current.right, a_list)

    def is_leaf(self, current):
        return current.left is None and current.right is None

    def sum_leaves(self):
        return self.sum_leaves_aux(self.root)

    def sum_leaves_aux(self, current):
        if current is None:
            return 0
        elif current.right is None and current.left is None:
            return current.key
        else:
            return self.sum_leaves_aux(current.right) + self.sum_leaves_aux(current.left)

    def _add_aux(self, current, item, bitstring_iterator):
        if current is None:
            current = TreeNode()
        try:
            bit = next(bitstring_iterator)
            if bit == "0":
                current.left = self._add_aux(current.left, item, bitstring_iterator)
            elif bit == "1":
                current.right = self._add_aux(current.right, item, bitstring_iterator)
        except StopIteration:
            current.item = item
        return current

    def print_preorder(self):
        self._print_preorder_aux(self.root)

    def _print_preorder_aux(self, current):
        if current is not None:
            print(current)
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)

    def print_inorder(self):
        self._print_inorder_aux(self.root)

    def _print_inorder_aux(self, current):
        if current is not None:
            self._print_preorder_aux(current.left)
            print(current)
            self._print_preorder_aux(current.right)

    def print_postorder(self):
        self._print_postorder_aux(self.root)

    def _print_postorder_aux(self, current):
        if current is not None:
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)
            print(current)
