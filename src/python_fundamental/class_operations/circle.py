import math

class Circle:
	radius: float
	# constructor of circle class
	def __init__(self, radius = 1):
		self.radius = radius

	def get_perimeter(self):
		return 2 * self.radius * math.pi

	def get_area(self):
		return math.sqrt(self.radius) * math.pi

	def set_radius(self, radius):
		self.radius = radius

circle = Circle(5)
print(circle.radius)
