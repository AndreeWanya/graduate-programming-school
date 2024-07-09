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
            	if node.next is None and node.prev is None:
            		self.head = None
            		self.tail = None
            		node = node.next
            	elif node.next is None:
            		self.tail = node.prev
            		node = node.next
            	elif node.prev is None:
            		self.head = node.next
            		node = node.next
            	else:
            		node.value = node.next.value
            		node.next = node.next.next
            	if all == False:
            		break
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
        if afterNode is not None:
            afterNode = afterNode.value
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode and node.next is not None:
                    newNode.next = node.next
                    node.next = newNode
                    break
                elif afterNode is None or (node.value == afterNode and node.next is None):
                    node.next = newNode
                    self.tail = newNode
                    break
                else:
                    node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            newNode.next = self.head.next
        self.head = newNode
        
        