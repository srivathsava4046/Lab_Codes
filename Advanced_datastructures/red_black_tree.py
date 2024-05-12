class Node:
    def __init__(self, key, parent=None, color=1):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color  # 1 for red, 0 for black

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None)  # Sentinel leaf nodes
        self.root = self.NIL_LEAF  # Initialize an empty tree

    def insert(self, key):
        new_node = Node(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        new_node.color = 1  # Red

        y = None
        x = self.root

        # Standard BST insert
        while x != self.NIL_LEAF:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
            self.root.color = 0  # Ensure the root is black
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is not None and new_node.parent.color == 1:
            self._insert_fixup(new_node)


    def _insert_fixup(self, node):
        while node.parent.color == 0:  # Red parent
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == 0:
                    # Case 1: Uncle is red
                    node.parent.color = 1  # Black
                    uncle.color = 1  # Black
                    node.parent.parent.color = 0  # Red
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Uncle is black, and node is a right child
                        node = node.parent
                        self._left_rotate(node)

                    # Case 3: Uncle is black, and node is a left child
                    node.parent.color = 1 # Black
                    node.parent.parent.color = 0  # Red
                    self._right_rotate(node.parent.parent)

            else:
                uncle = node.parent.parent.left

                if uncle.color == 1:
                    # Case 1: Uncle is red
                    node.parent.color = 0  # Black
                    uncle.color = 0  # Black
                    node.parent.parent.color = 1  # Red
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Uncle is black, and node is a left child
                        node = node.parent
                        self._right_rotate(node)

                    # Case 3: Uncle is black, and node is a right child
                    node.parent.color = 0  # Black
                    node.parent.parent.color = 1  # Red
                    self._left_rotate(node.parent.parent)

        self.root.color = 0  # Ensure root is black

    def delete(self, key):
        node = self.search(key)
        if node is not None:
            self._delete(node)

    def _delete(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL_LEAF:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL_LEAF:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 0:
            self._delete_fixup(x)

    def _delete_fixup(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                sibling = node.parent.right

                if sibling.color == 1:
                    # Case 1: Sibling is red
                    sibling.color = 0  # Black
                    node.parent.color = 1  # Red
                    self._left_rotate(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    # Case 2: Sibling is black, and both children are black
                    sibling.color = 1  # Red
                    node = node.parent
                else:
                    if sibling.right.color == 0:
                        # Case 3: Sibling is black, left child is red, and right child is black
                        sibling.left.color = 0  # Black
                        sibling.color = 1  # Red
                        self._right_rotate(sibling)
                        sibling = node.parent.right

                    # Case 4: Sibling is black, right child is red
                    sibling.color = node.parent.color
                    node.parent.color = 0  # Black
                    sibling.right.color = 0  # Black
                    self._left_rotate(node.parent)
                    node = self.root

            else:
                sibling = node.parent.left

                if sibling.color == 1:
                    # Case 1: Sibling is red
                    sibling.color = 0  # Black
                    node.parent.color = 1  # Red
                    self._right_rotate(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == 0 and sibling.right.color == 0:
                    # Case 2: Sibling is black, and both children are black
                    sibling.color = 1  # Red
                    node = node.parent
                else:
                    if sibling.left.color == 0:
                        # Case 3: Sibling is black, right child is red, and left child is black
                        sibling.right.color = 0  # Black
                        sibling.color = 1  # Red
                        self._left_rotate(sibling)
                        sibling = node.parent.left

                    # Case 4: Sibling is black, left child is red
                    sibling.color = node.parent.color
                    node.parent.color = 0  # Black
                    sibling.left.color = 0  # Black
                    self._right_rotate(node.parent)
                    node = self.root

        node.color = 0  # Ensure root is black

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node == self.NIL_LEAF or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node != self.NIL_LEAF:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.color))
            self._inorder_traversal(node.right, result)

# Usage example
if __name__ == "__main__":
    rbt = RedBlackTree()
    keys = [50, 30, 70, 20, 40, 60, 80, 10, 45]

    for key in keys:
        rbt.insert(key)

    print("Inorder Traversal:")
    for node in rbt.inorder_traversal():
        print(f"Key: {node[0]}, Color: {'Red' if node[1] == 1 else 'Black'}")

    delete_key = 30
    rbt.delete(delete_key)
    print(f"Deleted key {delete_key}")

    print("Inorder Traversal after deleting:")
    for node in rbt.inorder_traversal():
        print(f"Key: {node[0]}, Color: {'Red' if node[1] == 1 else 'Black'}")
