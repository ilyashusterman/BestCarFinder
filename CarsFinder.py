from finders_apis.Yad2Api import Yad2Api


class ApiQuery(object):

	def __init__(self, car_name):
		self.car_name = car_name

	def get_dict_params(self):
		return {
			'car_name': self.car_name
		}


class CarsFinder(object):

	def __init__(self):
		self.yad2_api = Yad2Api()

	def search_cars(self, name):
		car_results = self.yad2_api.search(ApiQuery(car_name=name))
