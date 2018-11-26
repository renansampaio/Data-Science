import scipy.spatial.distance as dist
import csv
import random
import numpy as np
import sys

data = []
data_class = np.genfromtxt('file.csv', delimiter=',')
clusters = []
data = data_class[:,0:8]
k = 2
att = len(data[0])
centroides = []
rep = True
mudou = 0
distance = np.zeros(shape=(len(data)-1))
centroides.append(random.randint(0,len(data)))
print(len(distance))
print(centroides[0])
X=data
for i in range(1,k):
	
	del X[centroides[0]]
	print(len(X))
	dist_min = float('inf')
	for j in range(len(X)):
		for c in range(len(centroides)):
			dst = dist.euclidean(X[j],data[centroides[c]])
			if dst<dist_min:
				dst_min=dst
		distance[j]=dist_min

	print(distance)
