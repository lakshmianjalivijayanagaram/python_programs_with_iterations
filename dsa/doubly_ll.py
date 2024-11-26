class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None
class doublyll:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end='---->')
                n=n.nref
    def print_ll_rev(self):
        if self.head is None:
            print('dll is empty')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end="----->")
                n=n.pref
    def add_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.nref=self.head
            self.head.pref=newnode
            self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=newnode
            newnode.pref=n
    def add_after(self,data,x):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                else:
                    n=n.nref
        if n is None:
            print('node not found')
        else:
            newnode=Node(data)
            newnode.nref=n.nref
            newnode.pref=n
            if n.nref is not None:
                n.nref.pref=newnode
            n.nref=newnode
    def



            
dl=doublyll()
dl.add_begin(10)
dl.add_begin(20)
dl.add_end(1111)
dl.add_after(123,20)
dl.print_ll()
dl.print_ll_rev()







