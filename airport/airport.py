from plane import Plane
import unittest

class Airport(object):

    def __init__(self):
        self.planes = []
        self.plane = Plane()

    def land_plane(self):
        self.planes.append(self.plane)
