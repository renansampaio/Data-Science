import os
import random
import numpy as np

numIndividuos=20

rodadas=1

numSementes=2

populacao = np.zeros((numIndividuos,5), dtype=float) #4 atributos mais precisao
'atributos = [minNo optmizations checkError usePrunning]'
'minNo = randint(2,50)'
'optmizations = randint(2,50)'
'checkError = randint(0,1)'
'usePrunning = randint(0,1)'

#funcao para calcular a precisao dos individuos da populacao
def calculaFuncao(matriz,numIndividuos):
	for x in range(numIndividuos):
		for y in range(numSementes):
	
			inicio = 'java -classpath weka.jar weka.classifiers.rules.JRip -F 10 -N '
			meio = ' -O '
			semente = ' -S ' 
			final1 = ' -t '
			ConjuntoDeDados = 'diabetes.arff'
			final2 = ' -p 0 > saida.txt'

			seed = random.randint(0,1000)

			#checagem para checkError e usePrunning
			if (matriz[x][2] == 0):
				check = ' -E'
			else:
				check = ''

			if (matriz[x][3] == 0):
				use = ' -P'
			else:
				use = ''

			string = inicio + str(int(matriz[x][0])) + meio + str(int(matriz[x][1])) + semente + str(seed) + check + use + final1 + ConjuntoDeDados + final2
			print(string)
			os.system(string)

			#calcula precisao do arquivo saida.txt
			with open('saida.txt','r') as file:
				count = 0
				while True:
					char = file.read(1)
					if not char: break
					if char=='+':
						count += 1
				matriz[x][4] += (1-(count/786.0))
		matriz[x][4]=matriz[x][4]/float(numSementes) #media das 5 sementes

	print(matriz)
	return matriz

#randomizacao dos parametros
for x in range(numIndividuos):
	populacao[x][0] = random.randint(2,50)
	populacao[x][1] = random.randint(2,50)
	populacao[x][2] = random.randint(0,1)
	populacao[x][3] = random.randint(0,1)

#primeira populacao de individuos
populacao=calculaFuncao(populacao,numIndividuos)

for rodada in range(rodadas):
####################SELECAO##################	
	#selecao de subconjuntos (particiona em 4) da populacao para o torneio entre si
	n = 4
	sub_conj = numIndividuos / n
	maior_valor = 0.0
	posicao = 0
	indice = [] #armazena os indices dos melhores de cada subconjunto
	count = 0
	for i in range(numIndividuos):
		if (populacao[i][4] > maior_valor): #checa se individuo atual possui maior precisao que o maior ate entao
				maior_valor = populacao[i][4]
				posicao = i

		if (((i+1)%n) == 0): #a cada subconjunto 
			indice.append(posicao)
			count = count + 1
			maior_valor = 0.0
	print(indice)


	melhores = np.zeros((int(sub_conj),5), dtype=float)
	for i in range(sub_conj):
		melhores[i]=populacao[indice[i]] #recupera os melhores individuos de cada subconjunto
	print(melhores) 


####################CROSSOVER##################
	nova_populacao = np.zeros((int(numIndividuos),5), dtype=float)
	for i in range(numIndividuos):
		if i<sub_conj:
			nova_populacao[i]=melhores[i]#armazena os melhores individuos dos subconjuntos no comeco da matriz
		else:
			for j in range(4):
				nova_populacao[i][j] = melhores[random.randint(0,sub_conj-1)][j] #novos individuos sao gerados a partir dos melhores




	print(nova_populacao)

####################MUTACAO##################
	mutacao=random.randint(1,4)#esolhe uma pequena parcela dos novos individuos pra sofrer mutacaoo
	mutantes=np.random.permutation(numIndividuos-sub_conj)#faz uma permutacao pra saber qual individuo novo ira ser modificado
	mutantes=mutantes[:mutacao]#escolhe os individuos que serao modificados

	for mutante in mutantes:
		atributo=random.randint(0,3)#escolhe randomicamento o atributo a ser modificado
		if atributo== 0 or 1:
			nova_populacao[mutante+sub_conj][atributo]=random.randint(2,50)
		else:
			nova_populacao[mutante+sub_conj][atributo]=random.randint(0,1)
							#esse shift e feito porque os primeiros individuos nao sofrerao mutacao

####################NOVA POPULACAO##################
	filhos=nova_populacao[sub_conj:numIndividuos] #parcela da nova populacao e separada para calcular a precisao
	print(nova_populacao)
	print(filhos)


	filhos=calculaFuncao(filhos,numIndividuos-sub_conj) #calcula precisao dos filhos
	nova_populacao[sub_conj:numIndividuos]=filhos #reagrupa os filhos de volta com a precisao calculada
	print(nova_populacao)

	aleatorio=np.random.permutation(numIndividuos) #embaralha a populacao para a proxima rodada
	nova_populacao=nova_populacao[aleatorio,:]

	print(nova_populacao)
	populacao=nova_populacao #proxima rodada
	print(populacao)

melhor_precisao= populacao[:,4]
melhor_indice=np.argmax(melhor_precisao)
print('Melhor individuo: ')
print(populacao[melhor_indice])
	# mudar seed

