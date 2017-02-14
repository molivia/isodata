#!/usr/bin/env python3

import isodata
import matplotlib
matplotlib.use('SVG') 
import matplotlib.pyplot as plt

# displays original, not clusterized points
def origin():
	x = [] # array for x coordinates
	y = [] # array for y coordinates

	# get points from module 'isodata.py'
	for point in isodata.points:
		x.append(point[0])
		y.append(point[1])
	"""
	for i in range(len(isodata.points)):
		x.append(isodata.points[i][0])
		y.append(isodata.points[i][1])
		"""

	plt.plot(x, y, linestyle='None', marker='o')
	#plt.axis([-10, 10, -10, 10])
	plt.grid()

	# display origin axis
	ax = plt.subplot()
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')

	plt.savefig('origin.png')


def clusterized():
	clusters = isodata.clusterize()
	#plt.plot()
	

	colors = ['b', 'g', 'r', 'c', 'm', 'k']
	markers = ['o', '^', '+', '*', 's']
	# iterating through all clusters
	for c, cluster in enumerate(clusters):
		x = []
		y = []
		for point in cluster:
			x.append(point[0])
			y.append(point[1])

		plt.plot(x,y, linestyle='None', marker=markers[c], c=colors[c], markerfacecolor='None')
		plt.grid()

	#plt.axis([-10, 10, -10, 10])

	plt.savefig('clusters.png')


if __name__ == "__main__":
	clusterized()



