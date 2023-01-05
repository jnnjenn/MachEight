import unittest
from app import app

class TestPairFinder(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(app([], 5), [])
    
    def test_no_pairs(self):
        self.assertEqual(app([1, 2, 3, 4], 5), [])
    
    def test_one_pair(self):
        self.assertEqual(app([1, 2, 3, 4], 5), [(1, 4)])
    
    def test_multiple_pairs(self):
        self.assertEqual(app([1, 2, 3, 4], 5), [(1, 4), (2, 3)])
    
    def test_negative_numbers(self):
        self.assertEqual(app([-1, -2, 3, 4], -3), [(-1, -2)])

    def test_one_numbers(self):
        self.assertEqual(app([1,9,5,0,20,-4,12,16,7], 12), [(5, 7), (0, 12), (-4, 16)])
    
if __name__ == '__main__':
    unittest.main()