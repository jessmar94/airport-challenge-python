# import unittest
# # import Airport as AirportClass
# # import Plane as PlaneClass
# from airport import Airport
# from plane import Plane
#
# class TestAirport(unittest.TestCase):
#
#     airport = Airport()
#     plane = Plane()
#
#     def test_land_place(self):
#         """
#         Test that plane added to planes list when lands
#         """
#         airport.land_plane()
#         self.assertEqual(self.planes, 4)
#         # self.assertEqual(self.planes(), [plane])
#
# if __name__ == '__main__':
#     unittest.main()

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
        self.airport.land_plane()
        self.assertEqual(self.airport.planes, [self.plane])

if __name__ == '__main__':
    unittest.main()
