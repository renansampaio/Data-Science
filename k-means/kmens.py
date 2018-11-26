import scipy.spatial.distance as dist
import csv
import random
import numpy as np

data = []
k = 2
rep = 0
data = np.genfromtxt('file.csv', delimiter=',')

att = len(data[0])
centroides = np.zeros(shape=(k,att), dtype=float)
clusters = []
print(data)

for x in range(k):
	centroides[x] = random.choice(data)

while (rep < 20):
	for x in range(k):
		clusters.append([])
	for i in range(len(data)):
		dist_min = float('inf')
		for p in range(len(centroides)):
			distancia = dist.euclidean(data[i],centroides[p])	
			if (distancia < dist_min):
				dist_min = distancia
				centroide_escolhido = p
		clusters[centroide_escolhido].append(i)

	for i in range(k):
		print("Cluster {}: {}".format(i+1,clusters[i]))

	print(centroides)

	soma_clusters = np.zeros(shape=(k,att), dtype=float)
	
	for i in range(k):
		for p in range(len(clusters[i])):
			soma_clusters[i] = np.add(soma_clusters[i],data[clusters[i][p]])
		centroides[i] = np.divide(soma_clusters[i],len(clusters[i]))

	print(len(clusters[0]))
	print(len(clusters[1]))
	print(soma_clusters)
	print(centroides)
	rep = rep + 1
