import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):

    def test_random(self):
        self.assertEqual(quicksort([3,6,8,10,1,2,1]), [1,1,2,3,6,8,10])


if __name__ == '__main__':
    unittest.main()
