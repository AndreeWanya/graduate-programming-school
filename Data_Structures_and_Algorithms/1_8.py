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
        if self.head is not None:
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
            
def LinkedLists2(l_list1, l_list2):
    node_1 = l_list1.head
    node_2 = l_list2.head
    result = []
    if node_1 is None and node_2 is None:
        return []
    if node_1 is None or node_2 is None:
        return None
    while node_1 is not None:
        result.append(node_1.value + node_2.value)
        if (node_1.next is None and node_2.next is not None) or (node_1.next is not None and node_2.next is None):
            return None
        node_1 = node_1.next
        node_2 = node_2.next
    return result
        
    
#s_list1 = LinkedList()
#s_list2 = LinkedList()
#list1 = []
#list2 = []
#
#for n in list1:
#    s_list1.add_in_tail(Node(n))
#for n in list2:
#    s_list2.add_in_tail(Node(n))
#
#s_list1.print_all_nodes()
#print()
#s_list2.print_all_nodes()
#
#print(LinkedListsSum(s_list1, s_list2))

