import unittest
from random import randint


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


class DeleteTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.delete(randint(1, 1000))
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.delete(55)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 88)
        s_list.delete(88)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 12)
    
    def test_one_item_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.delete(55)
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)
        s_list.delete(12)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
        
class DelAllTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.delete(randint(1, 1000), True)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.delete(55, True)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 88)
        s_list.delete(12, True)
        self.assertEqual(s_list.head.value, 128)
        self.assertEqual(s_list.tail.value, 88)
    
    def test_one_item_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.delete(55)
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)
        s_list.delete(12)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
        
class ListPurgeTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
    
    def test_one_item_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.clean()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
    

class FindAllTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList()
        nf = s_list.find_all(12)
        self.assertEqual(nf, [])
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        nf = s_list.find_all(12)
        self.assertEqual(len(nf), 2)
    
    def test_one_item_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        nf = s_list.find_all(12)
        self.assertEqual(len(nf), 1)
        nf = s_list.find_all(128)
        self.assertNotEqual(len(nf), 1)
        
        
class ListLenTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList()
        ll = s_list.len()
        self.assertEqual(ll, 0)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        ll = s_list.len()
        self.assertEqual(ll, len(test_list))
    
    def test_one_item_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        ll = s_list.len()
        self.assertEqual(ll, 1)
        
        
class InsertTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.insert(None, Node(randint(1, 1000)))
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)
        s_list.insert(None, Node(12))
        self.assertEqual(s_list.head.value, 12)
        self.assertIsNotNone(s_list.tail)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.insert(None, Node(34))
        s_list.insert(Node(88), Node(21))
        self.assertEqual(s_list.head.value, 34)
        self.assertEqual(s_list.tail.value, 21)
    
    def test_one_item_list(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(12))
        s_list.insert(None, Node(76))
        s_list.insert(Node(12), Node(40))
        self.assertEqual(s_list.head.value, 76)
        self.assertEqual(s_list.tail.value, 40)
        
        
if __name__ == '__main__':
    unittest.main()

