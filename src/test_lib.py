import pandas as pd
import unittest
from lib import DataProcessor
class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()
        self.data = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                                  'B': [5, 4, 3, 2, 1]})
        self.processor.data = self.data

    def test_load_data_from_csv(self):
        file_path = '../data/insurance.csv'
        self.processor.load_data_from_csv(file_path)
        self.assertIsNotNone(self.processor.data)

    def test_calculate_mean(self):
        column_name = 'A'
        expected_mean = self.data[column_name].mean()
        self.assertAlmostEqual(self.processor.calculate_mean(column_name), expected_mean)

    def test_calculate_median(self):
        column_name = 'B'
        expected_median = self.data[column_name].median()
        self.assertEqual(self.processor.calculate_median(column_name), expected_median)

    def test_calculate_std_dev(self):
        column_name = 'A'
        expected_std_dev = self.data[column_name].std()
        self.assertAlmostEqual(self.processor.calculate_std_dev(column_name), expected_std_dev)

    def test_generate_histogram(self):
        column_name = 'A'
        self.assertIsNone(self.processor.generate_histogram(column_name))

    def test_generate_bar_chart(self):
        x_column = 'A'
        y_column = 'B'
        self.assertIsNone(self.processor.generate_bar_chart(x_column, y_column))

if __name__ == '__main__':
    unittest.main()