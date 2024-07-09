class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

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
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    node = node.next
                elif node.next is not None:
                    node.value = node.next.value
                    node.next = node.next.next
                    if all == False:
                        node = None
                else:
                    node.prev.next = None
                    self.tail = node.prev
                    node = None
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
            self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode:
                    newNode.next = node.next
                    node.next = newNode
                    break
                elif node.next is None:
                    node.next = newNode
                    self.tail = node.next
                    break
                else:
                    node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None
        self.head = newNode
        
        