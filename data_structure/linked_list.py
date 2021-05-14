# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.start = None  

    def insertLastNode(self,value):
        newNode = Node(value)
        if(self.start == None):
            self.start = newNode 
        else:
            temp = self.start
            # print(temp)
            while temp.next != None:
                temp = temp.next
                print(temp) 
            temp.next = newNode


    def insertAtBeginning(self, new_data): 
  
    # 1 & 2: Allocate the Node & 
    #        Put in the data 
        new_node = Node(new_data) 
          
    # 3. Make next of new Node as head 
        new_node.next = self.start 
          
    # 4. Move the head to point to new Node  
        self.start = new_node 




    # This function is in LinkedList class.  
# Inserts a new node after the given prev_node. This method is  
# defined inside LinkedList class shown above */  
    


    def viewList(self):
        if self.start == None:
             print("list is empty")
        else:
            temp = self.start  # is storing stating address of node
            while temp != None:  # check next is not none
                print(temp.data,end=" ") #printing data
                temp = temp.next   #moving pointer to next


    def deleteFirst(self):
        if self.start == None:
            print("list is empty")
        else:
            self.start = self.start.next

l = LinkedList()
l.insertLastNode(1)
l.insertLastNode(2)
l.insertLastNode(3)
l.insertAfter(0,1)
# l.insertLastNode(3)
# l.insertLastNode(4)
# l.viewList()
# l.deleteFirst()
l.viewList()
