import unittest
from testing.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Aayush Nepal' works?"""
        formatted_name = get_formatted_name('aayush', 'nepal')
        self.assertEqual(formatted_name, 'Aayush Nepal')
    
    def test_first_middle_last_name(self):
        """Do names like 'Hari Bahadur Rana' works?"""
        formatted_name = get_formatted_name(first='hari', middle='bahadur', last='rana')
        self.assertEqual(formatted_name, 'Hari Bahadur Rana')

if __name__ == '__main__':
    unittest.main()
