"""

buying:   vhigh, high, med, low.
maint:    vhigh, high, med, low.
doors:    2, 3, 4, 5more.
persons:  2, 4, more.
lug_boot: small, med, big.
safety:   low, med, high.
class:    unacc, acc, good, vgood

buying:   3, 2, 1, 0.
maint:    3, 2, 1, 0.
doors:    2, 3, 4, 5.
persons:  2, 4, 5.
lug_boot: 0, 1, 2.
safety:   0, 1, 2.
class:    0, 1, 2, 3

"""

import csv
import random as rand
import numpy as np
import math

def distance(vet1, vet2):
	dist = [(a - b)**2 for a, b in zip(vet1, vet2)]
	dist = math.sqrt(sum(dist))
	return dist

data = np.genfromtxt('car.csv', delimiter=',')
Acertos_rodadas	=[]
matriz_melhor = np.zeros(shape=(4,4))
matriz_pior = np.zeros(shape=(4,4))
melhor_taxa = 0
pior_taxa = 10000
Taxa_classes_Global = []
Taxa_media_global = [0,0,0,0]
total_classes = [0,0,0,0]
rodadas = 100

for rep in range(rodadas):
	data_treino = []
	data_teste = []
	acertos = 0
	erros = 0
	total_acertos_classes = [0,0,0,0]
	total_erros_classes = [0,0,0,0]
	taxa_acertos_classes = [0,0,0,0]
	soma_treino = np.zeros(shape=(4,len(data[0])-1),dtype=float)
	matriz = np.zeros(shape=(4,4))
	soma_classe = np.zeros(shape=(4,len(data[0])-1),dtype=float)
	centroides = np.zeros(shape=(4,len(data[0])-1),dtype=float)

	porcent_treino = 0.5	
	count = [0,0,0,0]


	np.random.shuffle(data)

	tamanho_treino = round(porcent_treino*len(data))
	tamanho_teste = len(data) - tamanho_treino

	for i in range(tamanho_treino):
		data_treino.append(data[i])

	for i in range(tamanho_treino,len(data)):
		data_teste.append(data[i])		

	for i in range(len(data_treino)):
		if ((data_treino[i][6])==0):
			soma_classe[0] = np.add(soma_classe[0],data_treino[i][0:6]) 
			count[0] += 1
		elif ((data_treino[i][6])==1):
			soma_classe[1] = np.add(soma_classe[1],data_treino[i][0:6]) 
			count[1] += 1
		elif ((data_treino[i][6])==2):
			soma_classe[2] = np.add(soma_classe[2],data_treino[i][0:6]) 
			count[2] += 1
		elif ((data_treino[i][6])==3):
			soma_classe[3] = np.add(soma_classe[3],data_treino[i][0:6]) 
			count[3] += 1

	for p in range(4):
		centroides[p] = np.divide(soma_classe[p],count[p])

	for x in range(tamanho_teste):
		dist_min = float('inf')
		for n in range(len(centroides)):
			dst = distance(data_teste[x][0:6],centroides[n])
			if (dst < dist_min):
				dist_min = dst
				nova_classe = n
		if (data_teste[x][6]==nova_classe):
			acertos = acertos + 1
			matriz[int(nova_classe)][int(nova_classe)] = matriz[int(nova_classe)][int(nova_classe)] + 1
			total_acertos_classes[int(nova_classe)] += 1
		else:
			erros = erros + 1
			index = int(data_teste[x][6])
			matriz[index][int(nova_classe)] = matriz[index][int(nova_classe)] + 1
			total_erros_classes[index] += 1

	taxa_acertos = acertos/tamanho_teste
	taxa_erros = erros/tamanho_teste

	if (taxa_acertos > melhor_taxa):
		melhor_taxa	= taxa_acertos
		matriz_melhor = matriz	
	if (taxa_acertos < pior_taxa):
		pior_taxa = taxa_acertos
		matriz_pior = matriz

	for p in range(4):
		taxa_acertos_classes[p] = total_acertos_classes[p] / (total_acertos_classes[p] + total_erros_classes[p])

	print("Total de amostras de teste: {}".format(tamanho_teste))
	print("Acertos: {}".format(acertos))
	print("{}%".format(round(taxa_acertos,4)*100))
	print("Erros: {}".format(erros))
	print("{}%".format(round(taxa_erros,4)*100))
	Acertos_rodadas.append(taxa_acertos)
	Taxa_classes_Global.append(taxa_acertos_classes)


print(["%.4f" % v for v in Acertos_rodadas])
Media_Acertos = np.mean(Acertos_rodadas)
Mediana_Acertos = np.median(Acertos_rodadas)
Max_Acertos = np.max(Acertos_rodadas)
Min_Acertos = np.min(Acertos_rodadas)
Desvio_Padrao = np.std(Acertos_rodadas)

print("-----------------------------------\n")
print("Média de acertos: {} ".format(round(Media_Acertos,4)*100))
print("Mediana de acertos: {} ".format(round(Mediana_Acertos,4)*100))
print("Máximo de acertos: {} ".format(round(Max_Acertos,4)*100))
print("Mínimo de acertos: {} ".format(round(Min_Acertos,4)*100))
print("Desvio Padrão de acertos: {} ".format(round(Desvio_Padrao,4)*100))
print("Matriz de Confusão para Melhor Caso:\n")
print(matriz_melhor)
print("\nMatriz de Confusão para o Pior Caso:\n")
print(matriz_pior)

for j in range(rodadas):
	Taxa_media_global[0] += Taxa_classes_Global[j][0]
	Taxa_media_global[1] += Taxa_classes_Global[j][1]
	Taxa_media_global[2] += Taxa_classes_Global[j][2]
	Taxa_media_global[3] += Taxa_classes_Global[j][3]
Taxa_media_global = np.divide(Taxa_media_global,rodadas)

print("\nTaxa média das Clases (Classe 0, 1, 2 e 3): \n {}".format(Taxa_media_global))	