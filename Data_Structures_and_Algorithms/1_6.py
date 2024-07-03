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
        node = self.head
        while node is not None:
            if node.next is None and node.value == val:
                self.head = None
                self.tail = None
                break
            elif node.next is None:
                break
            elif node.value == val:
                node.value = node.next.value
                node.next = node.next.next
                if all==False:
                    break
            elif node.next.next is not None and node.next.value == val:
                node.next.value = node.next.next.value
                node.next.next = node.next.next.next
                if all==False:
                    break
            elif node.next.next is None and node.next.value == val:
                node.next = None
                self.tail = node
            else:
                node = node.next
            
                
    def clean(self):
        self.head = None
        self.tail = None
    
    def len(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        return counter
    
    def insert(self, afterNode, newNode):
        node = self.head
        while node is not None:
            if afterNode == None:
                break
            if node.value == afterNode.value:
                newNode.next = node.next
                node.next = newNode
                break
            node = node.next
        if newNode.next is None:
            self.tail = newNode
        if afterNode == None:
            self.head = newNode
            self.head.next = node

