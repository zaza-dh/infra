

class BinaryTree(object):
    __slots__ = ('value', 'parent', 'left_child', 'right_child')

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
            self.left_child.parent = self
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
            self.left_child.parent = self

    def insert_right(self, value):

        if self.right_child is None:
            self.right_child = BinaryTree(value)
            self.right_child.parent = self
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
            self.right_child.parent = self

    def find_root(self):
        node = self
        while self.parent is not None:
            node = self.parent
        return node


def height_of_tree(node):

    if node is None:
        return 0
    else:
        return max(height_of_tree(node.left_child), height_of_tree(node.right_child)) + 1


root = BinaryTree(5)
root.insert_left(2)
root.insert_right(3)
root.right_child.insert_right(1)
root.left_child.insert_right(6)
import pdb; pdb.set_trace()
root.order()
print(height(root))
print(root.value)
print(root.right_child.value)
print(root.left_child.value)

