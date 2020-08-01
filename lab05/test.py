from hashing import *
import unittest

class tests(unittest.TestCase):
	
	def test(self):
		H = HashTable() # Create a hash table, and chuck some values into it.
		H[54] = "cat"
		H[26] = "dog"
		H[93] = "lion"
		H[17] = "tiger"
		H[77] = "bird"
		H[31] = "cow"
		H[44] = "goat"
		H[55] = "pig"
		valBeforeResize = H[26]
		H[20] = "chicken"
		#once we add "chicken," we trigger a resize.
		valAfterResize = H[26]
		self.assertEqual(valBeforeResize, valAfterResize, "Expected output is True")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)