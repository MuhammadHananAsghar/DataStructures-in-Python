# LIFO
class Stack:
    def __init__(self, length :int) -> None:
        self.top = -1
        self.length =  length - 1
        self.stackList = []

    
    def addStackNode(self, value :int) -> None:
        if(self.top >= self.length):
            print("Stack Overflow")
        
        else:
            self.top = self.top + 1
            self.stackList.append(value)

    def popStackNode(self) -> None:
        if(self.top == -1):
            print("Stack Underflow")
        else:
            self.top = self.top - 1

    def displayStack(self) -> None:
        for i in reversed(range(self.top+1)):
            print("StackNode: ", self.stackList[i])


stack = Stack(4)
stack.addStackNode(1)
stack.addStackNode(2)
stack.addStackNode(3)
stack.addStackNode(4)
stack.displayStack()
print("Popping")
stack.popStackNode()
stack.displayStack()