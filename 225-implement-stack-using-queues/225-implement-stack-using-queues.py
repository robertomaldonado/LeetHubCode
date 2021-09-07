class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list_ = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.list_:
            self.list_.append(x)
        else:
            self.list_ = [x]

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.list_.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.list_[len(self.list_)-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.list_: 
            if len(self.list_) > 0: 
                return False
        return True
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()