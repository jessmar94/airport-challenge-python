import unittest
from airport.airport import Airport
from airport.plane import Plane

class TestAirport(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = Plane()

    def test(self):
        self.assertTrue(True)

    def test_land_plane(self):
        self.airport.land_plane(self.plane)
        self.assertEqual(self.airport.planes, [self.plane])

if __name__ == '__main__':
    unittest.main()
