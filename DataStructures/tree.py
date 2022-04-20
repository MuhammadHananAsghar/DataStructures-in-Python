class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        pass

    def addNode(self, value):
        node = Node(value)
        return node

    def addLeft(self, node, value):
        node.left = value

    def addRight(self, node, value):
        node.right = value

    def inorder(self, root) -> None:
        # IN-ORDER
        # Left -> Root -> Right
        if root:
            self.inorder(root.left)

            print(root.value+" --> ", end="")

            self.inorder(root.right)

    def preorder(self, root) -> None:
        # PRE-ORDER
        # Root -> Left -> Right
        if root:
            print(root.value+" --> ", end="")

            self.preorder(root.left)

            self.preorder(root.right)

    def postorder(self, root) -> None:
        # POST-ORDER
        # Left -> Right -> Root
        if root:
            self.postorder(root.left)

            self.postorder(root.right)
            
            print(root.value+" --> ", end="")

    def display(self, command, root) -> None:
        if command == "in":
            print("\n*------------- Traversing IN-ORDER -----------*\n")
            self.inorder(root)

        if command == "pre":
            print("\n*------------- Traversing PRE-ORDER -----------*\n")
            self.preorder(root)

        if command == "post":
            print("\n*------------- Traversing POST-ORDER -----------*\n")
            self.postorder(root)
        
        print("")

tree = Tree()

phones = tree.addNode("Mobile Phones")

android = tree.addNode("Android")
iphone = tree.addNode("iphone")
tree.addLeft(phones, android)
tree.addRight(phones, iphone)

tree.display("in", phones)
tree.display("pre", phones)
tree.display("post", phones)

# tree.addLeft(iphone, "IPhone 12")
# tree.addRight(iphone, "IPhone 13")