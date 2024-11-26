class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_All(self):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end='------>')
                n=n.ref
    def Add_begin(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode
    def Add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            else:
                n=n.ref
        if n is None:
            print('node is n present in ll')
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode
    def del_begin(self):
        if self.head is None:
            print('ll is empty')
        else:
            self.head=self.head.ref
    def del_end(self):
        if self.head is None:
            print('ll is empty')
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def del_by_val(self,x):
        if self.head is None:
            print('ll is empty')
        if x==self.head.data:
            self.head=self.head.ref
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            else:
                n=n.ref
        if n.ref is None:
            print('the nod is not preset')
        else:
            n.ref=n.ref.ref
ll1=LinkedList()
#ll1.Add_begin(30)
ll1.Add_begin(20)
ll1.Add_begin(10)
#ll1.add_after(50,20)
ll1.Add_end(1000)
#ll1.del_begin()
#ll1.del_end()
ll1.del_by_val(10)
#ll1.Add_end(2000)
ll1.print_All()
