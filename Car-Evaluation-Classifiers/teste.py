import math
import scipy.spatial.distance as dist
import numpy as np


data = np.genfromtxt('car.csv', delimiter=',')
count = [0,0,0,0]
soma_classe = np.zeros(shape=(4,len(data[0])-1),dtype=float)
centroides = np.zeros(shape=(4,len(data[0])-1),dtype=float)
classe0 = []
classe1 = []
classe2 = []
classe3 = []

for i in range(len(data)):
	if ((data[i][6])==0):
		soma_classe[0] = np.add(soma_classe[0],data[i][0:6]) 
		count[0] += 1
		classe0.append(data[i][0:6])
	elif ((data[i][6])==1):
		soma_classe[1] = np.add(soma_classe[1],data[i][0:6]) 
		count[1] += 1
		classe1.append(data[i][0:6])
	elif ((data[i][6])==2):
		soma_classe[2] = np.add(soma_classe[2],data[i][0:6]) 
		count[2] += 1
		classe2.append(data[i][0:6])
	elif ((data[i][6])==3):
		soma_classe[3] = np.add(soma_classe[3],data[i][0:6]) 
		count[3] += 1
		classe3.append(data[i][0:6])

for p in range(4):
	centroides[p] = np.divide(soma_classe[p],count[p])


print(classe0)
print(classe1)
print(classe2)
print(classe3)
print(classe0)
cov0 = np.cov(classe0)
print(cov0)
matriz0 = np.linalg.pinv(cov0)


matriz1 = np.linalg.pinv(np.cov(classe1))
matriz2 = np.linalg.pinv(np.cov(classe2))
matriz3 = np.linalg.pinv(np.cov(classe3))


valor = ((data[0] - centroides[0]).transpose())*matriz0*(data[0] - centroides[0])
print(valor)
