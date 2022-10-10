import random
from models.point import Point

# A class used to create the set of points to use on CH Algorithm

# La classe PointsSet, qui génère avec la bibliothèque 
# "random" des ensembles de points selon les hypothèses de l'algorithme de Graham.
class PointsSet:

	def __init__(self):
		# Initial list of random points
		self.len_list = random.randint(100, 200)
		self.input_points = [(random.randint(0, 100),random.randint(0, 100)) for i in range(self.len_list)]
		self.input_points.append((0, 0))

		# Clean duplicates of the list
		self.input_points_clean = list(dict.fromkeys(self.input_points))

		# Create list of each x and y point separated to facilite the chart 
		self.points_x = [point[0] for point in self.input_points_clean]
		self.points_y = [point[1] for point in self.input_points_clean]

		# Final set of points
		self.points = []
		for point in self.input_points_clean:
			self.points.append(Point(point[0], point[1]))
