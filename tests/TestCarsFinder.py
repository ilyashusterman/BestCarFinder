from unittest import TestCase

from CarsFinder import CarsFinder


class TestCarsFinder(TestCase):

	def setUp(self):
		self.cars_finder = CarsFinder()

	def test_initiating_car_finders(self):
		self.cars_finder = CarsFinder()

	def test_search_subaru_cars(self):
		cars = self.cars_finder.search_cars(name='subaru')
		self.assertIsInstance(cars, list)