class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        pass

    def addRoot(self, data):
        root = Node(data)
        return root

    def addNode(self, root, data):
        if data == root.value:
            print("Node Present")
            return
        
        if data < root.value:
            if root.left:
                self.addNode(root.left, data)
            else:
                root.left = Node(data)

        else:
            if root.right:
                self.addNode(root.right, data)
            else:
                root.right = Node(data)

    def findMin(self, root):
        if root.left is None:
            return root.value
        return self.findMin(root.left)

    def findMax(self, root):
        if root.right is None:
            return root.value
        return self.findMax(root.right)
    
    def deleteNode(self, root, value):
        if root.value is None:
            return root

        elif value < root.value:
            if root.left:
                root.left = self.deleteNode(root.left, value)
        
        elif value > root.value:
            if root.right:
                root.right = self.deleteNode(root.right, value)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            if root.right is None:
                temp = root.left
                root = None
                return temp


            temp = self.findMin(root.right)
            root.value = temp.value
            root.right = self.deleteNode(root.right, temp.value)
            
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)

            print(str(root.value)+" --> ", end="")

            self.inorder(root.right)


bst = BST()

root = bst.addRoot(25)
bst.addNode(root, 14)
bst.addNode(root, 13)
bst.addNode(root, 26)
bst.addNode(root, 56)
bst.addNode(root, 7)
bst.addNode(root, 12)
bst.addNode(root, 44)
bst.addNode(root, 32)
print("\nTRAVERSING")
bst.inorder(root)
print("\n")
print("After Deleteing")
nRoot = bst.deleteNode(root, 12)
print("\nTRAVERSING")
bst.inorder(nRoot)
print("\n")
print("Minimum: {}".format(bst.findMin(root)))
print("Maximum: {}".format(bst.findMax(root)))