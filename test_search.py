from plot_gtex import linear_search
from plot_gtex import binary_search
import unittest


class TestSearch(unittest.TestCase):
    """
    This class is used to test the linear and binary search methods.

    """
    # Test for when key exists in the list
    def test_linear_exists(self):
        self.key = 5
        self.data_list = list(range(10))
        self.assertEqual(linear_search(self.key, self.data_list), 5)

    # Test for when key does not exist in the list
    def test_linear_missing(self):
        self.key = 100
        self.data_list = list(range(10))
        self.assertEqual(linear_search(self.key, self.data_list), -1)

    # Test for when key is a string
    def test_linear_bad_key(self):
        self.key = '5'
        self.data_list = list(range(10))
        self.assertEqual(linear_search(self.key, self.data_list), -1)

    # Test for when key is None
    def test_linear_no_key(self):
        self.key = None
        self.data_list = list(range(10))
        self.assertEqual(linear_search(self.key, self.data_list), -1)

    # Test for when list is empty
    def test_linear_empty(self):
        self.key = 5
        self.data_list = []
        self.assertEqual(linear_search(self.key, self.data_list), -1)

    # Test for when key exists in the list
    def test_binary_exists(self):
        self.key = 5
        self.data_list = list(zip(range(10), range(10)))
        self.assertEqual(binary_search(self.key, self.data_list), 5)

    # Test for when key does not exist in the list
    def test_binary_missing(self):
        self.key = 100
        self.data_list = list(zip(range(10), range(10)))
        self.assertEqual(binary_search(self.key, self.data_list), -1)

    # Test for when key is a string
    def test_binary_bad_key(self):
        self.key = '5'
        self.data_list = list(zip(range(10), range(10)))
        self.assertRaises(TypeError and
                          SystemExit, binary_search, self.key, self.data_list)

    # Test for when key is None
    def test_binary_no_key(self):
        self.key = None
        self.data_list = list(zip(range(10), range(10)))
        self.assertRaises(TypeError and
                          SystemExit, binary_search, self.key, self.data_list)

    # Test for when list is empty
    def test_binary_empty(self):
        self.key = 5
        self.data_list = []
        self.assertEqual(binary_search(self.key, self.data_list), -1)


if __name__ == '__main__':
    unittest.main()
