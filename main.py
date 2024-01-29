from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        size = self.q.qsize()
        self.q.put(x)
        self.rotate(size)

    def pop(self) -> int:
        return self.q.get()

    # Rotate the queue to place the new element at the front
    def rotate(self,size):
        for _ in range(size):
            self.q.put(self.q.get())
    
    def top(self) -> int:
        # Retrieve the front element
        top = self.q.get()
        # Immediately put it back
        self.q.put(top)
        size = self.q.qsize()
        self.rotate(size-1)
        return top

    def empty(self) -> bool:
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
