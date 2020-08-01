from sorting import *

import unittest

class TestSquare(unittest.TestCase):

    def test_sort(self):
    	# Check to see if both methods sort correctly
        list1 = [54,26,93,17,77,31,44,55,20]
        list2 = [54,26,93,17,77,31,44,55,20]
        quickSort(list1)
        mo3_quickSort(list2)
        sorted = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        self.assertEqual(list1, sorted)
        self.assertEqual(list2, sorted)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)