import unittest

from flatten_list import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty(self):
        incoming = []
        expected = []
        self.assertEqual(flatten_list(incoming), expected)

    def test_flat(self):
        incoming = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_list(incoming), expected)

    def test_single_nest(self):
        incoming = [[1, 2], [3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_list(incoming), expected)

    def test_multiple_nests(self):
        incoming = [1, 2, [3, 4, [5, 6, [7, 8]]], 9, [10, [11, 12]]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten_list(incoming), expected)

    def test_wrong_type_in_list(self):
        other_types = [None, 'string', True, {1: 2}]

        # Test when passed in as list (ie an item in the list)
        for item in other_types:
            with self.assertRaises(Exception) as ex:
                flatten_list([[1, 2], 3, item])

            self.assertEqual(
                ex.exception.args[0],
                "Unexpected object type in list. Got {}, expected int or list.".format(type(item))
            )

    def test_wrong_type_passed_in(self):
        other_types = [None, 'string', True, {1: 2}]

        # Test when passed in as the object (ie not passing a list in)
        for item in other_types:
            with self.assertRaises(Exception) as ex:
                flatten_list(item)

            self.assertEqual(
                ex.exception.args[0],
                "Object passed to function is {}, not a list".format(type(item))
            )


if __name__ == '__main__':
    unittest.main()
