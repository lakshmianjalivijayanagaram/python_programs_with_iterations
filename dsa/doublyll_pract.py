#ouput=[5,4,3]
#print(" ".join(map(str,ouput)))
#print(map(str,ouput))

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublyll:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'---->',end=' ')
                n=n.next
    def print_ll_rev(self):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            while n is not None:
                print(n.data,'---->',end=' ')
                n=n.prev
    def add_begin(self,data):
        newnode=Node(data)
        if self.head is None:
           self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newnode
            newnode.prev=n
    def add_after(self,data,x):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                else:
                    n=n.next
        if n is None:
            print('node not Found')
        else:
            newnode=Node(data)
            newnode.next=n.next
            newnode.prev=n
            if n.next is not None:
                n.next.prev=newnode
            n.next=newnode
            
ll=doublyll()
#ll.insert_empty(111)
#ll.add_begin(10)
ll.add_begin(11)
ll.add_end(1111)
ll.add_after(123,1111)
ll.print_ll()
ll.print_ll_rev()

