import unittest
from random import randint
import sorting

class MyTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sorted(sorting.result), sorting.sorting_list(sorting.result, sorting.n, sorting.m))

    def test_random(self):
        for i in range(100000):
            n = randint(0, 100)
            m = n
            result = sorting.create_list(n, m)
            self.assertEqual(sorted(sorting.result), sorting.sorting_list(sorting.result, sorting.n, sorting.m))

    def test_null(self):
        n = 0
        m = n
        result = sorting.create_list(n, m)
        self.assertEqual(sorted(sorting.result), sorting.sorting_list(sorting.result, sorting.n, sorting.m))


    def test_max(self):
        n = 10000000     # При введении достаточно большого значения (например 9223372036854775808), компьютер зависает намертво
        m = n
        result = sorting.create_list(n, m)
        self.assertEqual(sorted(sorting.result), sorting.sorting_list(sorting.result, sorting.n, sorting.m))


if __name__ == '__main__':
    unittest.main()
