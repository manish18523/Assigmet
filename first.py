
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
    
class linkedList:
    def __init__(self):
        self.head=None

# 1.1 Adding a new Node into  right side of Linked List.
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)
    
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end='-->>')
            temp=temp.next
        print('None')


# 1.4 Display the total memory space occupied by the linked list
    def display(self):
        count=0
        temp=self.head
        while temp:
            temp=temp.next
            count+=1
        return 2*count

# 1.2 Deleting a particular node (referenced by the location),

    def deleteNode(self,ind):
        
        if ind==1:
            temp=self.head.next
            self.head=None
            self.head=temp
        
        temp=self.head
        for i in range(ind-2):
            temp=temp.next
        
        temp.next=temp.next.next
 

# 1.5 Delete all the nodes from the list 
# which contain a particular data say a number 5 and the next subsequent node.

    def deleteFurther(self,data):
        if self.head.data==data:
            self.head=None
            return

        temp=self.head
        while temp.next:
            if temp.next.data==data:
                temp.next=None
            else:
                temp=temp.next


# 1.3 Delete all the nodes from the list which contain a particular data say a number 5

    def deleteParticular(self,data):
        if self.head.data==data:
            self.head=self.head.next
            return self.deleteParticular(data)
            

        temp=self.head
        while temp.next:
            if temp.next.data==data:
                temp.next=temp.next.next
            else:
                temp=temp.next



if __name__ == "__main__":
          
    l=linkedList()
    print('Dry Run to Add Nodes at the end of linked List (Q-1.1) ') 
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.append(7)
    l.append(3)
    l.append(5)
    l.append(6)
    l.append(3)
    l.append(3)
    l.append(7)

    l.printList()
    print('Dry run to Deleting a particular node (referenced by the location) (Q-1.2) Node(index=5) ')
    l.deleteNode(5)
    l.printList()
    print('Dry run to Delete all the nodes from the list which contain a particular data say a number 3.(Q-1.5) ')
    l.deleteParticular(3)
    l.printList()
    print('Dry run Delete all the nodes from the list which contain a \nparticular data say a number 4 and the next subsequent node.')
    l.deleteFurther(4)
    l.printList()
    print('Adding new Node with value=19')
    l.append(19)
    l.printList()
    print('Dry run to Display the total memory space occupied by the linked list (Q-1.4) ')
    print('Total  Memory Used data+pointer = ',l.display())

    l.printList()