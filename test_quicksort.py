import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):

    def test_sorted(self):
        self.assertEqual(quicksort([1,2,3,4,5]), [1,2,3,4,5])

    def test_reverse_sorted(self):
        self.assertEqual(quicksort([5,4,3,2,1]), [1,2,3,4,5])


    def test_empty(self):
        self.assertEqual(quicksort([]), [])

if __name__ == '__main__':
    unittest.main()
