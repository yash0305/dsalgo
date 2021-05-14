# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedList:
#     def __init__(self):
#         self.head = None

#     def inserthead(self,newNode):
#         temporaryNode = self.head
#         self.head = newNode
#         self.head.next = temporaryNode
#         del temporaryNode

#     def printNode(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         else:
#             current = self.head
#             while current != None:
#                 print(f"{current.data} --> ",end="")
#                 current  = current.next


#     def insertAtEnd(self,newNode):
#         if self.head is None: 
#             self.inserthead(newNode)
#             return    
#         else:
#             lastNode = self.head
#             while lastNode.next != None:

#                 lastNode = lastNode.next
#                 lastNode.next = newNode
#                 return


#     def length(self):
#         length = 0
#         current = self.head
#         while current != None:
#             length += 1
#             current = current.next
#         return length

#     def deleteLast(self):
#         lastNode = self.head
#         while lastNode.next != None:
#             previousNode  = lastNode
#             lastNode = lastNode.next
#         previousNode.next = None

# first = Node(1)
# second = Node(2)
# third  = Node(3)
# l = linkedList()
# l.inserthead(first)
# l.inserthead(second)
# l.insertAtEnd(third)
# l.deleteLast()
# l.printNode()



class node():
    def __init__(self,data):
        self.data = data 
        self.next = None

class l:
    def __init__(self):
        self.head = None


    def append(self,data):
        new = node(data)
        if self.head is None:
            self.head = new
            return 
        else:    
            cur = self.head 
            while cur.next is not None:
                cur = cur.next
            cur.next = new
            
    def prepend(self,data):
        new = node(data)
        if self.head is None:
            self.head = new
            return
        else:
            cur = self.head
            new.next = cur
            self.head = new
             
        
    def printLlist(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
            
    def lengthnode(self):
        count = 0
        cur = self.head
        while cur is not None:
            count+=1
            cur = cur.next
        return count
            
    def deletebetween(self,position,key):
        cur = self.head
        currentPosition = 0
        while cur is not None:
            
            if currentPosition == key:
                
                
                
                
                break
            else:
                prev = cur
                cur = cur.next
                currentPosition+=1
                
        
            
    def atEnd(self):
        cur = self.head
        while cur.next is not None:
            prev = cur  
            cur = cur.next 
        prev.next = None
        
    
    def inBetween(self,key,data):
        new = node(data)
        cur = self.head
        num = 0
        while cur is not None:
            
            if num == key:
                prev.next = new
                new.next = cur
                break
            else:
                prev = cur
                cur = cur.next
                num+=1
                
        return num ,cur.data,prev
        
        
    def last(self):
        cur = self.head
        while cur is not None:
            prev = cur.data 
            cur = cur.next 
        return prev
        
    
            
        


li = l()
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append (5)
li.append('yash')
li.append(6)
print('in',li.inBetween(3,7))
print('length',li.lengthnode())
# li.deletebetween (2)
#li.atEnd()
li.printLlist()
print("--------")


print(li.last())

