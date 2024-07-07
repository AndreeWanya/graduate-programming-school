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
            if node.value == val and node.next is not None:
                node.value = node.next.value
                node.next = node.next.next
                if all==False:
                    break
            elif node.value == val and node.next is None:
                if node.prev is not None:
                    node.value = node.prev.value
                    node.next = None
                else:
                    self.head = None
                    self.tail = None
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
            if node.next is not None:
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
            self.head = newNode
        else:
            newNode.next = self.head.next
            self.head = newNode
            
import unittest
        
class FindTests(unittest.TestCase):
        
    def test_empty_list(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        node = s_list.find(38)
        self.assertNotEqual(node, 38)
        self.assertEqual(node, None)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
            
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList2()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        node = s_list.find(55)
        self.assertEqual(node.value, 55)
        node = s_list.find(88)
        self.assertEqual(node.value, 88)
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.tail.value, 88)
            
    def test_one_item_list(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(12))
        node = s_list.find(55)
        self.assertIsNone(node)
        node = s_list.find(12)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 12)
            
class FindAllTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        nodes = s_list.find_all(38)
        self.assertNotEqual(nodes, [Node(38)])
        self.assertEqual(nodes, [])
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
            
    def test_full_list(self):
        
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList2()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        nodes = s_list.find_all(55)
        self.assertEqual(nodes[0].value, 55)
        nodes = s_list.find_all(12)
        self.assertEqual(nodes[1].value, 12)
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.tail.value, 88)
        
    def test_one_item_list(self):
        
        s_list = LinkedList2()
        s_list.add_in_tail(Node(12))
        nodes = s_list.find_all(55)
        self.assertEqual(nodes, [])
        nodes = s_list.find_all(12)
        self.assertIsNotNone(nodes)
        self.assertEqual(nodes[0].value, 12)
        
class DelTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.delete(38)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList2()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.delete(55)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 88)
        s_list.delete(88)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 12)
    
    def test_one_item_list(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(12))
        s_list.delete(55)
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)
        s_list.delete(12)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
class DelAllTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.delete(64, True)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList2()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.delete(55, True)
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 88)
        s_list.delete(12, True)
        self.assertEqual(s_list.head.value, 128)
        self.assertEqual(s_list.tail.value, 88)
    
    def test_one_item_list(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(12))
        s_list.delete(55)
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)
        s_list.delete(12)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        
class InsertTests(unittest.TestCase):
    
    def test_empty_list(self):
        s_list = LinkedList2()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        s_list.insert(None, Node(15))
        self.assertEqual(s_list.head.value, 15)
        self.assertEqual(s_list.tail.value, 15)
        
    def test_full_list(self):
        test_list = [55, 12, 128, 12, 88]
        s_list = LinkedList2()
        for num in test_list:
            s_list.add_in_tail(Node(num))
        s_list.insert(None, Node(34))
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.tail.value, 34)
        s_list.insert(Node(34), Node(21))
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.tail.value, 21)
    
    def test_one_item_list(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(12))
        s_list.insert(None, Node(76))
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 76)
        
class AddInHeadTests(unittest.TestCase):
    
    def test_empty_list(self):
        pass

if __name__ == '__main__':
     unittest.main()