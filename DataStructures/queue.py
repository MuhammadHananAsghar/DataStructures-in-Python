# FIFO
class Queue:
    def __init__(self, length :int) -> None:
        self.length = length - 1
        self.queueList = []
        self.rear = -1
        self.front = -1
        self.ptr = ""

    def enqueue(self, value :int) -> None:
        if(self.rear >= self.length):
            print("Queue Overflow.")
        
        else:
            self.front = 0
            self.rear = self.rear + 1
            self.queueList.append(value)

    def dequeue(self) -> None:
        if(self.front == -1) and (self.rear == -1):
            print("No Queue Found")
        else:
            self.front = self.front + 1

    def displayQueue(self) -> None:
        if(self.front == -1) and (self.rear == -1):
            print("No Queue Found")
        else:
            self.ptr = ""
            self.ptr += "Front "
            for i in range(self.front, self.rear+1):
                self.ptr += f"---[{self.queueList[i]}]---"
            self.ptr += " Rear"
            print(self.ptr)
            print("")

queue = Queue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.displayQueue()
print("Dequeued.")
queue.dequeue()
queue.displayQueue()