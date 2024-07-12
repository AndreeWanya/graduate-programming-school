class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        
#n1 = Node(12)
#n2 = Node(55)
#n1.next = n2
#n2.prev = n1

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None and node.next is None:
                    self.head = None
                    self.tail = None
                    break
                elif node.prev is not None and node.next is not None:
                    node.value = node.next.value
                    node.next = node.next.next
                    if all == False:
                        break
                elif node.next is None:
                    self.tail = node.prev
                    self.tail.next = None
                    break
                else:
                    self.head = node.next
                    self.head.prev = None
                    if all == False:
                        break
                    node = self.head
            else:
                node = node.next            

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.head = newNode
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        elif afterNode is None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    newNode.next = node.next
                    node.next = newNode
                    if newNode.next is None:
                        self.tail = newNode
                    break
                else:
                    node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None            
        self.head = newNode
        
