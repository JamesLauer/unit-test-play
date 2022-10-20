import unittest
from import_data import import_data


class TestSum(unittest.TestCase):
    def test_column_num(self):
        """
         Tests presence column names in input data csv file
         """
        result = import_data()
        self.assertIn('city', result[0])
        self.assertIn('region', result[0])
        self.assertIn('country', result[0])
        self.assertIn('country_code', result[0])
        self.assertIn('latitude', result[0])
        self.assertIn('longitude', result[0])
        self.assertIn('timezone', result[0])

    def test_names_len(self):
        """
        Tests number of columns
        """
        desired_names = [
            'city',
            'region',
            'country',
            'country_code',
            'latitude',
            'longitude',
            'timezone'
        ]
        result = len(import_data()[0])
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()