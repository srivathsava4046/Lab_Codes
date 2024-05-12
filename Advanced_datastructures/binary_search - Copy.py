class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        
        return root
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)


    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._get_min_value(root.right)
            root.right = self._delete(root.right, root.key)

        return root

    def _get_min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, root, result):
        if root:
            result.append(root.key)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        
        return result

    def _postorder_traversal(self, root, result):
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.key)

# Function to display the menu and perform actions
def menu():
    bst = BinarySearchTree()
    keys = [44, 86, 23, 32, 64, 10, 5, 11]

    for key in keys:
        bst.insert(key)
    while True:
        print("\nBinary Search Tree Menu:")
        print("1. Insert an element")
        print("2. Search for an element")
        print("3. Delete an element")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            key = int(input("Enter the value to insert: "))
            bst.insert(key)
            print("Inorder Traversal:", bst.inorder_traversal())
            print("Preorder Traversal:", bst.preorder_traversal())
            print("Postorder Traversal:", bst.postorder_traversal())
        elif choice == "2":
            key = int(input("Enter the value to search: "))
            if bst.search(key):
                print(f"{key} found in the BST")
                print("Inorder Traversal:", bst.inorder_traversal())
                print("Preorder Traversal:", bst.preorder_traversal())
                print("Postorder Traversal:", bst.postorder_traversal())
            else:
                print(f"{key} not found in the BST")
                print("Inorder Traversal:", bst.inorder_traversal())
                print("Preorder Traversal:", bst.preorder_traversal())
                print("Postorder Traversal:", bst.postorder_traversal())
        elif choice == "3":
            key = int(input("Enter the value to delete: "))
            bst.delete(key)
            print(f"Deleted {key} from the BST")
            print("Inorder Traversal:", bst.inorder_traversal())
            print("Preorder Traversal:", bst.preorder_traversal())
            print("Postorder Traversal:", bst.postorder_traversal())
            
        elif choice == "4":
           
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()
