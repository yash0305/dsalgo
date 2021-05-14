from collections import deque

class queue:
    def __init__(self):
        self.buffer = deque()
        

    def push(self,value):
        self.buffer.appendleft(value)

    def pop(self):
        return self.buffer.pop()


    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def view(self):
        for i in enumerate((len(self.container)-1),-1,-1):
            return print(self.container[i],end="")
       

q = queue()
q.push({
    "Name" : "yash",
    "id" : 1 
})

q.push({
    "Name" : "riddhi",
    "id" : 2 
})

q.push({
    "Name" : "avi",
    "id" : 3
})

print(q.is_empty())