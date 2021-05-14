from collections import deque

stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()
        

    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def view(self):
        for i in range((len(self.container)-1),-1,-1):
            return self.container[i]
       


new = Stack()
new.push("avyan")
new.push("ira")


print(new.view())