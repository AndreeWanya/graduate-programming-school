import unittest
from random import randint, choices
from first_task import LinkedList, Node

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
        
        
        
if __name__ == '__main__':
    unittest.main()

