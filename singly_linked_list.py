class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("linked list is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
ll1=linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_end(100)
ll1.print_LL()