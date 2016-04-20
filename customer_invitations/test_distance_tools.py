import unittest
import math

from distance_tools import calculate_distance, coords_degs_to_radians, filter_by_distance


class TestDegtoRadianConverter(unittest.TestCase):

    def test_wrong_input_type(self):
        exception_msg = "Input is not a dict"

        with self.assertRaises(AssertionError) as ex:
            coords_degs_to_radians((1, 2))

        self.assertEqual(ex.exception.args[0], exception_msg)

    def test_missing_latitude(self):
        exception_msg = "Input is missing latitude value"

        with self.assertRaises(AssertionError) as ex:
            coords_degs_to_radians({'longitude': 3})

        self.assertEqual(ex.exception.args[0], exception_msg)

    def test_missing_longitude(self):
        exception_msg = "Input is missing longitude value"

        with self.assertRaises(AssertionError) as ex:
            coords_degs_to_radians({'latitude': 3})

        self.assertEqual(ex.exception.args[0], exception_msg)

    #  since we use the inbuilt radian conversion, we are really testing that
    #  latitude and longitude are the correct output (eg incase they get mixed up)
    def test_conversion(self):
        incoming = {
            'latitude': -45,
            'longitude': 90,
        }

        expected_output = {
            'latitude': math.pi * -.25,
            'longitude': math.pi * .5,
        }

        self.assertDictEqual(coords_degs_to_radians(incoming), expected_output)


class TestDistanceCalculator(unittest.TestCase):

    def test_london_nyc(self):
        # coordinates taken from Google:
        # https://www.google.com/?q=london%20lat%20long
        # https://www.google.com/?q=new%20york%20lat%20long
        london = {
            'latitude': 51.5074,
            'longitude': 0.1278,
        }
        nyc = {
            'latitude': 40.7128,
            'longitude': 74.0059,
        }

        # 5570km taken from http://www.distancefromto.net/distance-from/London/to/New+York
        self.assertEqual(round(calculate_distance(london, nyc), 0), 5570)

    def test_same_point(self):
        london = {
            'latitude': 51.5074,
            'longitude': 0.1278,
        }

        self.assertEqual(calculate_distance(london, london), 0)


class TestFilterByDistance(unittest.TestCase):

    def test_filter(self):
        input_list = [
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
        fixed_coord = {
            'latitude': 45.0683241,
            'longitude': -15.266502,
        }
        max_km = 305

        expected_output = [{
            'latitude': 45.231932,
            'user_id': 2,
            'name': 'Tim Berners-Lee',
            'longitude': -19.123989,
        }]

        self.assertListEqual(
            filter_by_distance(input_list, fixed_coord, max_km),
            expected_output
        )

if __name__ == '__main__':
    unittest.main()
