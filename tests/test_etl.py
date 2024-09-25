import unittest
import pandas as pd
from utils import transform_data

class TestETL(unittest.TestCase):
    def test_transform_data(self):
        raw_data = pd.DataFrame({'existing_column': [1, 2, 3]})
        transformed_data = transform_data(raw_data)
        self.assertIn('new_column', transformed_data.columns)

if __name__ == '__main__':
    unittest.main()
