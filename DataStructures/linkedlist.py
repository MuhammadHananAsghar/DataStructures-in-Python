class Node:
    def __init__(self, value :str) -> None:
        self.value = value
        self.Next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.id = 1

    def addAtEnd(self, value: str) -> None:
        nNode = Node(value)
        if self.head is None:
            self.head = nNode
            return
        node = self.head
        while(node.Next):
            node = node.Next
        node.Next = nNode

    def addAtStart(self, value: str) -> None:
        nNode = Node(value)
        if self.head is None:
            self.head = nNode
            return
        nNode.Next = self.head
        self.head = nNode

    def addAfterSpecPos(self, posValue: str, value :str) -> None:
        nNode = Node(value)
        if self.head is None:
            self.head = nNode
            return
        node = self.head
        while(node.value != posValue):
            node = node.Next
        temp = node.Next
        node.Next = nNode
        nNode.Next = temp

    def reverseLinkedList(self) -> None:
        current = self.head
        previous, next = None, None
        while(current is not None):
            next = current.Next
            current.Next = previous
            previous = current
            current = next

        self.head = previous

    def printLinkedList(self) -> None:
        node = self.head
        while node is not None:
            print(f"""
            Node: {self.id}
            |{(len("Value: ")+len(node.value))*"-"}|{(len("Address: ")+len(hex(id(node.Next))))*"-"}|
            |Value: {node.value}|Address: {hex(id(node.Next))}|
            |{(len("Value: ")+len(node.value))*"-"}|{(len("Address: ")+len(hex(id(node.Next))))*"-"}|"""
            )
            self.id += 1
            node = node.Next


linkedList = LinkedList()
linkedList.addAtEnd("2")
linkedList.addAtEnd("4")
linkedList.addAtEnd("5")
linkedList.addAtStart("1")
linkedList.addAfterSpecPos("2", "3")
linkedList.reverseLinkedList()
linkedList.printLinkedList()