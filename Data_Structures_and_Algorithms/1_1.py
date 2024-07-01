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
        return []
    
    def delete(self, val, all=False):
        node = self.head
        if node.next == None and node.value == val:
            self.head = None
            self.tail = None
        while node is not None:
            if node.next != None:
                if node.value == val:
                    node.value = node.next.value
                    node.next = node.next.next
                    break
                elif node.next.next == None and node.next.value == val:
                    node.next = None
                    self.tail = node
                else:
                    node = node.next
            else:
                node = node.next                
                
    def clean(self):
        pass
    
    def len(self):
        return 0
    
    def insert(self, afterNode, newNode):
        pass
    
