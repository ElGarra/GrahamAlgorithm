from functools import cmp_to_key
from models.point import Point

# A class used to define some utility functions and the main Graham Scan Algorithm

# La classe GrahamAlgorithm, qui simule toute la logique de l'algorithme.
# Il s'agit notamment des fonctions de tri, de recherche, de push et de pop.
class GrahamAlgorithm:

	def __init__(self, points):
		self.points = points
		self.n = len(self.points)

		# A global point needed for sorting points with reference
		# to the first point
		self.p0 = Point(0, 0)
		self.ch_points_x = [] # List of x coordinates of the points conforming the convex hull
		self.ch_points_y = [] # List of x coordinates of the points conforming the convex hull

	# A utility function to find next to top in a stack
	def nextToTop(self, S):
		return S[-2]

	# A utility function to return square of distance
	# between p1 and p2
	def distSq(self, p1, p2):
		return ((p1.x - p2.x) * (p1.x - p2.x) +
				(p1.y - p2.y) * (p1.y - p2.y))

	# To find orientation of ordered triplet (p, q, r).
	# The function returns following values
	# 0 --> p, q and r are collinear
	# 1 --> Clockwise
	# 2 --> Counterclockwise
	# More info in https://www.geeksforgeeks.org/orientation-3-ordered-points/
	def orientation(self, p, q, r):
		val = ((q.y - p.y) * (r.x - q.x) -
			(q.x - p.x) * (r.y - q.y))
		if val == 0:
			return 0 # collinear
		elif val > 0:
			return 1 # clock wise
		else:
			return 2 # counterclock wise

	# A function used by cmp_to_key function to sort an array of
	# points with respect to the first point
	def compare(self, p1, p2):
		o = self.orientation(self.p0, p1, p2) # Find orientation
		if o == 0:
			if self.distSq(self.p0, p2) >= self.distSq(self.p0, p1):
				return -1
			else:
				return 1
		else:
			if o == 2:
				return -1
			else:
				return 1

	# Prints convex hull of a set of n points.
	def convexHull(self):

		# Find the bottommost point
		ymin = self.points[0].y
		min = 0
		for i in range(1, self.n):
			y = self.points[i].y

			# Pick the bottom-most or choose the left
			# most point in case of tie
			if ((y < ymin) or
				(ymin == y and self.points[i].x < self.points[min].x)):
				ymin = self.points[i].y
				min = i

		# Place the bottom-most point at first position
		self.points[0], self.points[min] = self.points[min], self.points[0]

		# Sort n-1 points with respect to the first point.
		# A point p1 comes before p2 in sorted output if p2
		# has larger polar angle (in counterclockwise
		# direction) than p1
		self.p0 = self.points[0]
		self.points = sorted(self.points, key=cmp_to_key(self.compare))

		# If two or more points make same angle with p0,
		# Remove all but the one that is farthest from p0
		# Remember that, in above sorting, our criteria was
		# to keep the farthest point at the end when more than
		# one points have same angle.
		m = 1 # Initialize size of modified array
		for i in range(1, self.n):
		
			# Keep removing i while angle of i and i+1 is same
			# with respect to p0
			while ((i < self.n - 1) and
			(self.orientation(self.p0, self.points[i], self.points[i + 1]) == 0)):
				i += 1

			self.points[m] = self.points[i]
			m += 1 # Update size of modified array

		# If modified array of points has less than 3 points,
		# convex hull is not possible
		if m < 3:
			return

		# Create an empty stack and push first three points
		# to it.
		S = []
		S.append(self.points[0])
		S.append(self.points[1])
		S.append(self.points[2])

		

		# Process remaining n-3 points
		for i in range(3, m):
		
			# Keep removing top while the angle formed by
			# points next-to-top, top, and points[i] makes
			# a non-left turn
			while ((len(S) > 1) and
			(self.orientation(self.nextToTop(S), S[-1], self.points[i]) != 2)):
				S.pop()
			S.append(self.points[i])


		# Now stack has the output points,
		# print contents of stack
		while S:
			p = S[-1]
			# print("(" + str(p.x) + ", " + str(p.y) + ")")
			self.ch_points_x.append(p.x)
			self.ch_points_y.append(p.y)
			S.pop()

	def print_ch_points(self):
		for i in range(len(self.ch_points_x)):
			print(f"Le point ({self.ch_points_x[i]}, {self.ch_points_y[i]}) fait partie de l'enveloppe convexe !")
