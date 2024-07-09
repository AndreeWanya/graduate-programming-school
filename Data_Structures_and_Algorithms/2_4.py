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
        pass

    def len(self):
        return 0

    def insert(self, afterNode, newNode):
        pass

    def add_in_head(self, newNode):
        pass