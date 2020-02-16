from TreeNode import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None


    def __delitem__(self, key, item):
        self.root = self._delitem_aux_(self.root, key, item)

    def _delitem_aux_(self, key, root):
        #Base Case
        if root is None:
            return root

        # If key to be deleted is smaller than root's key, then
        # key should be in left subtree

        if key < root.key:
            root.left = deleteNode(root.left, key)

        # If key to be deleted is greater than root's key, then
        # key should be in right subtree

        elif key > root.key:
            root.right = deleteNode(root.right, key)

        # if key same as root key, then this is node to be deleted
        else:

            #Node with one child or no child
            if root.left is none:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            #Node with two children

