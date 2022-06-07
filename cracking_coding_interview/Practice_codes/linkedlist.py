#Program is to write linked list having 3 nodes

#create node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#create Linked list class having node object and traverse the linked list
class linkedlist:
    def __init__(self):
        self.head=None
    def traverselinkedlist(self):
        print("inside traverselinkedlist")
        temp=self.head
        while (temp):
            print(temp.data)
            print(temp.next)
            temp=temp.next

if __name__=='__main__':

    llist=linkedlist()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.head.next=second
    second.next=third
    #traverse through linked list
    llist.traverselinkedlist()

    