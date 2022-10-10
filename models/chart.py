import matplotlib.pyplot as plt

# Et finalment, la classe Chart, qui permet de tracer les points dans l'espace et l'enveloppe convexe.
class Chart:
	
	def __init__(self, points_x, points_y, ch_points_x, ch_points_y):
		self.points_x = points_x
		self.points_y = points_y
		self.ch_points_x = ch_points_x
		self.ch_points_y = ch_points_y


	def create_chart(self):
		self.last_x = self.ch_points_x[0]
		self.last_y = self.ch_points_y[0]
		self.ch_points_x.append(self.last_x)
		self.ch_points_y.append(self.last_y)
		plt.scatter(self.points_x, self.points_y)
		plt.title('Convex Hull of the given points')
		plt.xlabel("X axis")
		plt.ylabel("Y axis")
		plt.plot(self.ch_points_x, self.ch_points_y, label = "convex hull", color='orange')
		plt.legend()
		plt.show()

