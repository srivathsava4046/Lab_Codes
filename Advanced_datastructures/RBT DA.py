class Node:
    def __init__(self, key, color, parent, left, right, size=1):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
        self.size = size


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 'black', None, None, None, 0)
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = Node(key, 'red', None, self.NIL_LEAF, self.NIL_LEAF, 1)
        self._insert(new_node)

    def _insert(self, node):
        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            parent.size += 1
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def delete(self, key):
        z = self._search(key)
        if z is not None:
            self._delete(z)

    def _delete(self, z):
        y = z
        y_original_color = y.color

        if z.left == self.NIL_LEAF:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL_LEAF:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self._fix_delete(x)

    def select(self, k):
        if 0 < k <= self.root.size:
            return self._select(self.root, k)
        else:
            return None

    def _select(self, node, k):
        left_size = node.left.size if node.left != self.NIL_LEAF else 0

        if k == left_size + 1:
            return node.key
        elif k <= left_size:
            return self._select(node.left, k)
        else:
            return self._select(node.right, k - left_size - 1)

    def search(self, key):
        node = self._search(key)
        return node.key if node is not None else None

    def _search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node == self.NIL_LEAF or key == node.key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def _minimum(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL_LEAF:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.NIL_LEAF:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

        x.size = y.size
        y.size = y.left.size + y.right.size + 1

    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = 'black'

    def _fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = 'black'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent
        if v != self.NIL_LEAF:
            v.size = u.size

    def view_tree(self):
        print("Red-Black Tree:")
        self.print_tree(self.root)

    def print_tree(self, node, level=0, prefix="Root: "):
        if node != self.NIL_LEAF:
            print(" " * (level * 4) + prefix + f"{node.key} ({node.color}, Size: {node.size})")
            self.print_tree(node.left, level + 1, "L--- ")
            self.print_tree(node.right, level + 1, "R--- ")

def switch_operation(rb_tree, operation):
    if operation == 1:
        rb_tree.view_tree()
    elif operation == 2:
        key = int(input("Enter the key to insert: "))
        rb_tree.insert(key)
        print("Red-Black Tree after insertion:")
        rb_tree.view_tree()
    elif operation == 3:
        key = int(input("Enter the key to delete: "))
        rb_tree.delete(key)
        print("Red-Black Tree after deletion:")
        rb_tree.view_tree()
    elif operation == 4:
        key = int(input("Enter the key to search: "))
        result = rb_tree.search(key)
        if result is not None:
            print(f"Key {key} found in the Red-Black Tree.")
        else:
            print(f"Key {key} not found in the Red-Black Tree.")
    elif operation == 5:
        k = int(input("Enter k to find the k-th smallest element: "))
        result = rb_tree.select(k)
        if result is not None:
            print(f"The {k}-th smallest element is: {result}")
        else:
            print("Invalid value of k.")
    else:
        print("Invalid operation.")

# Main program to take user input and build the Red-Black Tree
if __name__ == "__main__":
    rb_tree = RedBlackTree()

    while True:
        try:
            print("\nChoose an operation:")
            print("1. View Tree")
            print("2. Insertion")
            print("3. Deletion")
            print("4. Searching")
            print("5. Selection (k-th smallest element)")
            print("6. Exit")
            operation = int(input("Enter the operation number: "))

            if operation == 6:
                break

            switch_operation(rb_tree, operation)

        except ValueError:
            print("Invalid input. Please enter a valid operation number.")
