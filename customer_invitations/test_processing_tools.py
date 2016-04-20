import unittest
import filecmp
import json

from processing_tools import parse_customer_json, ingest_file, sort_users_by_id, save_customers_to_file


class TestJsonParser(unittest.TestCase):

    def test_good_parse(self):
        """
        Test to check that the json string is parsed correctly
        """
        input = '{"latitude": "52.833502", "user_id": 25, "name": "David Behan", "longitude": "-8.522366"}'

        expected_output = {
            'user_id': 25,
            'name': 'David Behan',
            'latitude': 52.833502,
            'longitude': -8.522366,
        }

        self.assertDictEqual(parse_customer_json(input), expected_output)

    def test_invalid_latitude(self):
        input = """{"latitude": "fify-two", "user_id": 25, "name": "David Behan", "longitude": "-8.522366"}"""
        exception_msg = """Could not cast latitude to float (value: 'fify-two')"""

        with self.assertRaises(Exception) as ex:
            parse_customer_json(input)

        self.assertEqual(ex.exception.args[0], exception_msg)

    def test_invalid_longitude(self):
        input = """{"latitude": "52.833502", "user_id": 25, "name": "David Behan", "longitude": "-8.522366s"}"""
        exception_msg = """Could not cast longitude to float (value: '-8.522366s')"""

        with self.assertRaises(Exception) as ex:
            parse_customer_json(input)

        self.assertEqual(ex.exception.args[0], exception_msg)

    def test_missing_key(self):
        input = """{"latitude": "52.833502", "user_id": 25, "longitude": "-8.522366s"}"""
        exception_msg = """field 'name' missing in line: {"latitude": "52.833502", "user_id": 25, "longitude": "-8.522366s"}"""

        with self.assertRaises(Exception) as ex:
            parse_customer_json(input)

        self.assertEqual(ex.exception.args[0], exception_msg)

    def test_user_id_not_int(self):
        input = '{"latitude": "52.833502", "user_id": "25", "name": "David Behan", "longitude": "-8.522366"}'
        exception_msg = """user_id not an int in line: {"latitude": "52.833502", "user_id": "25", "name": "David Behan", "longitude": "-8.522366"}"""

        with self.assertRaises(Exception) as ex:
            parse_customer_json(input)

        self.assertEqual(ex.exception.args[0], exception_msg)


class TestFileIngestor(unittest.TestCase):

    def test_file_ingestor(self):
        # We expect it to skip one line due to a missing name
        expected_output = [
            {
                'latitude': 55.123546,
                'user_id': 1,
                'name': 'Vint Cerf',
                'longitude': -0.12389,
            },
            {
                'latitude': 45.231932,
                'user_id': 2,
                'name': 'Tim Berners-Lee',
                'longitude': -19.123989,
            },
        ]

        self.assertListEqual(ingest_file('test.json'), expected_output)


class TestSorter(unittest.TestCase):

    def test_sort(self):
        input = [
            {
                'latitude': 55.123546,
                'user_id': 3,
                'name': 'Vint Cerf',
                'longitude': -0.12389,
            },
            {
                'latitude': 45.231932,
                'user_id': 1,
                'name': 'Tim Berners-Lee',
                'longitude': -19.123989,
            },
            {
                'latitude': 23.412435,
                'user_id': 2,
                'name': 'Woz',
                'longitude': -12.127389,
            },
        ]
        expected_output = [
            {
                'latitude': 45.231932,
                'user_id': 1,
                'name': 'Tim Berners-Lee',
                'longitude': -19.123989,
            },
            {
                'latitude': 23.412435,
                'user_id': 2,
                'name': 'Woz',
                'longitude': -12.127389,
            },
            {
                'latitude': 55.123546,
                'user_id': 3,
                'name': 'Vint Cerf',
                'longitude': -0.12389,
            },
        ]

        self.assertListEqual(sort_users_by_id(input), expected_output)


class TestFileSave(unittest.TestCase):

    def test_save(self):
        input = [
            {
                'latitude': 45.231932,
                'user_id': 1,
                'name': 'Tim Berners-Lee',
                'longitude': -19.123989,
            },
            {
                'latitude': 23.412435,
                'user_id': 2,
                'name': 'Woz',
                'longitude': -12.127389,
            },
            {
                'latitude': 55.123546,
                'user_id': 3,
                'name': 'Vint Cerf',
                'longitude': -0.12389,
            },
        ]
        output_filename = 'test_customer_save.json'
        expected_output_filename = 'test_customer_save_expected.json'

        save_customers_to_file(input, output_filename)

        self.assertListEqual(
            ingest_file(output_filename),
            ingest_file(expected_output_filename)
        )


if __name__ == '__main__':
    unittest.main()
