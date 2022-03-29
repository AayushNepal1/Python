import unittest
from module.city_function import loaction

class LocationsTestCase(unittest.TestCase):
    """Test for 'name_function.py'"""

    def test_city_country(self):
        """Do city and country like 'Santiago Chile' works?"""
        place = loaction('santiago', 'chile')
        self.assertEqual(place, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Do city country and population like 'Santiago, Chile and Population' works?"""
        place = loaction('santiago', 'chile', '5000000')
        self.assertEqual(place, 'Santiago, Chile 5000000')

    
if __name__ == '__main__':
    unittest.main()
