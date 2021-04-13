class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._queue.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        x = self._queue[0]
        self._queue =  self._queue[1:]
        return x


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._queue[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if self._queue else False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()