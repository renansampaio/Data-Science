"""

buying:   vhigh, high, med, low. -> Preço de Compra
maint:    vhigh, high, med, low. -> Preço de Manutenção
doors:    2, 3, 4, 5more.		 -> Número de Portas
persons:  2, 4, more.			 -> Capacidade de Pessoas
lug_boot: small, med, big.		 -> Tamanho do bagageiro
safety:   low, med, high.		 -> Segurança do carro
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

def distance(vector1, vector2):
	dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
	dist = math.sqrt(sum(dist))
	return dist

rodadas = 100
Acertos_rodadas = []
Taxa_classes_Global = []
Taxa_media_global = [0,0,0,0]
matriz_melhor = np.zeros(shape=(4,4))
matriz_pior = np.zeros(shape=(4,4))
total_classes = [0,0,0,0]
data = np.genfromtxt('car.csv', delimiter=',')
melhor_taxa = 0
pior_taxa = 10000

for rep in range(rodadas):
	print("Rodada {}".format(rep))
	data_treino = []
	data_teste = []
	acertos = 0
	erros = 0
	total_acertos_classes = [0,0,0,0]
	total_erros_classes = [0,0,0,0]
	taxa_acertos_classes = [0,0,0,0]
	porcent_treino = 0.8
	matriz = np.zeros(shape=(4,4))
	np.random.shuffle(data)

	tamanho_treino = round(porcent_treino*len(data))
	tamanho_teste = len(data) - tamanho_treino


	for i in range(tamanho_treino):
		data_treino.append(data[i])

	for i in range(tamanho_treino,len(data)):
		data_teste.append(data[i])

	for x in range(tamanho_teste):
		dist_min = float('inf')
		for p in range(tamanho_treino):
			dst = distance(data_teste[x][0:6],data_treino[p][0:6])
			if (dst < dist_min):
				dist_min = dst
				nova_classe = data_treino[p][6]
		if (data_teste[x][6]==nova_classe):
			acertos = acertos + 1
			matriz[int(nova_classe)][int(nova_classe)] +=  1
			total_acertos_classes[int(nova_classe)] += 1
			
		else:
			erros = erros + 1
			index = int(data_teste[x][6])
			matriz[index][int(nova_classe)] += 1
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

	#print("Total Erros Classe: {}".format(total_erros_classes))
	#print("Total Acertos Classe: {}".format(total_acertos_classes))
	#print("Taxa de Acertos por Classe: Classe 0 - {} Classe	1 - {} Classe 2 - {} Classe 3 - {}".format(taxa_acertos_classes[0],taxa_acertos_classes[1],taxa_acertos_classes[2],taxa_acertos_classes[3]))
	print("Total de amostras de teste: {}".format(tamanho_teste))
	print("Acertos: {}".format(acertos))
	print("{}%".format(round(taxa_acertos,4)*100))
	print("Erros: {}".format(erros))
	print("{}%".format(round(taxa_erros,4)*100))
	Acertos_rodadas.append(taxa_acertos)
	Taxa_classes_Global.append(taxa_acertos_classes)

Media_Acertos = np.mean(Acertos_rodadas)
Mediana_Acertos = np.median(Acertos_rodadas)
Max_Acertos = np.max(Acertos_rodadas)
Min_Acertos = np.min(Acertos_rodadas)
Desvio_Padrao = np.std(Acertos_rodadas)
print("-----------------------------------\n")
print("Taxa de acerto por rodada:")
print(["%.4f" % v for v in Acertos_rodadas])
print("\n Média de acertos: {} \n".format(round(Media_Acertos,4)*100))
print("Mediana de acertos: {} \n".format(round(Mediana_Acertos,4)*100))
print("Máximo de acertos: {} \n".format(round(Max_Acertos,4)*100))
print("Mínimo de acertos: {} \n".format(round(Min_Acertos,4)*100))
print("Desvio Padrão de acertos: {} \n".format(round(Desvio_Padrao,4)*100))
print("Matriz de Confusão para o Melhor Caso: \n {}".format(matriz_melhor))
print("\nMatriz de Confusão para o Pior Caso: \n {}".format(matriz_pior))

for j in range(rodadas):
	Taxa_media_global[0] += Taxa_classes_Global[j][0]
	Taxa_media_global[1] += Taxa_classes_Global[j][1]
	Taxa_media_global[2] += Taxa_classes_Global[j][2]
	Taxa_media_global[3] += Taxa_classes_Global[j][3]
Taxa_media_global = np.divide(Taxa_media_global,rodadas)

print("\nTaxa média das Clases (Classe 0, 1, 2 e 3): \n {}".format(Taxa_media_global))	