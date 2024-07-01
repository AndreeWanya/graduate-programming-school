class Node:
    
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        
    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
    
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    
    def find_all(self, val):
        nf = []
        node = self.head
        while node is not None:
            if node.value == val:
                nf.append(node)
            node = node.next
        return nf
    
    def delete(self, val, all=False):
        self.del_all(val, all)
        if self.tail is not None and self.tail.value == val:
            self.del_all(val, True)
        
    def del_all(self, val, all=False):
        node = self.head
        if node.next == None and node.value == val:
            self.head = None
            self.tail = None
        while node is not None:
            if node.next != None:
                if node.value == val and node.next != None:
                    node.value = node.next.value
                    node.next = node.next.next
                    if all == False:
                        break
                elif node.next.next == None and node.next.value == val:
                    node.next = None
                    self.tail = node
                else:
                    node = node.next
            else:
                node = node.next            
                
    def clean(self):
        self.head = None
        self.tail = None
    
    def len(self):
        return 0
    
    def insert(self, afterNode, newNode):
        pass
    
n1 = Node(55)
n2 = Node(12)
n1.next = n2		# 12 -> 55
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(88))
s_list.print_all_nodes()

#print()
#
#nf = s_list.find(55)
#if nf is not None:
#    print(nf.value)
    
#print()
    
#s_list.delete(12, True)
#s_list.print_all_nodes()

#print()
#print(s_list.head.value)
#print(s_list.tail.value)

#s_list.clean()

#print()
#print(s_list.head)
#print(s_list.tail)

nf = s_list.find_all(12)
for n in nf:
    print(n.value)
    print(n.next)