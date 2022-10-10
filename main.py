
###################################################################################################################################
###################################################################################################################################
###############			Program developed for Algorithm Design - MIE Electif of École Centrale de Marseille			###############
###############    by Joaquín Castaños, to find and create a chart of the convex Hull of a random set of points.    ###############
###################################################################################################################################
###################################################################################################################################

# Based on GeekForGeeks python3 https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
# program to find convex hull of a set of points. Refer
# https://www.geeksforgeeks.org/orientation-3-ordered-points/
# for explanation of orientation()

import time
from tqdm import tqdm
from models.points_set import PointsSet
from models.graham_algorithm import GrahamAlgorithm
from models.chart import Chart


# Notre implémentation Python comprend 4 classes qui nous permettent de simuler le programme :

# Si nous exécutons le programme plusieurs fois, nous pouvons voir les coordonnées 
# des points qui composent l'enveloppe convexe, et un graphique représentant l'enveloppe convexe.

if __name__ == "__main__":
	points_set = PointsSet()
	graham_algorithm = GrahamAlgorithm(points_set.points)
	graham_algorithm.convexHull()
	graham_algorithm.print_ch_points()
	print("\nCreating chart of the Convex Hull...\n")
    # Create progress bar to catch the atention on the terminal
	for i in tqdm(range(10)):
		time.sleep(0.5)
	print(" ")
	ch_chart = Chart(points_x= points_set.points_x, 
	points_y= points_set.points_y, ch_points_x= graham_algorithm.ch_points_x, 
	ch_points_y= graham_algorithm.ch_points_y)
	ch_chart.create_chart()