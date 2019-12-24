from plane import Plane
import unittest

class Airport(object):

    def __init__(self):
        self.planes = []
        plane = Plane()

    def land_plane(self, plane):
        self.planes.append(plane)
