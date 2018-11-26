import os
import numpy as np
import random 

for rep in range(1000):

	## Variáveis do código
	config = np.zeros((9), dtype=int)
	final = np.zeros((10), dtype=int)
	options = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
	matriz = np.zeros((3,3), dtype=int)
	boolean = True
	sair = True
	o_win = False
	x_win = False

	## Laço de jogo da velha aleatório
	for x in range(9):
		if (sair):
			escolha = random.choice(options)
			index , = np.where(options == escolha)
			options = np.delete(options,index[0])
			if(boolean):
				config[escolha] = 1
				boolean = False
				if ((config[0]==1 and config[1]==1 and config[2] ==1) or (config[3]==1 and config[4]==1 and config[5] ==1) or (config[6]==1 and config[7]==1 and config[8] ==1) or (config[0]==1 and config[3]==1 and config[6] ==1) or (config[1]==1 and config[4]==1 and config[7] ==1) or (config[2]==1 and config[5]==1 and config[8] ==1) or (config[0]==1 and config[4]==1 and config[8] ==1) or (config[2]==1 and config[4]==1 and config[6] ==1)):
					print("X ganhou!")
					x_win = True
					sair = False			
			else:
				config[escolha] = -1
				boolean = True
				if ((config[0]==-1 and config[1]==-1 and config[2] ==-1) or (config[3]==-1 and config[4]==-1 and config[5] ==-1) or (config[6]==-1 and config[7]==-1 and config[8] ==-1) or (config[0]==-1 and config[3]==-1 and config[6] ==-1) or (config[1]==-1 and config[4]==-1 and config[7] ==-1) or (config[2]==-1 and config[5]==-1 and config[8] ==-1) or (config[0]==-1 and config[4]==-1 and config[8] ==-1) or (config[2]==-1 and config[4]==-1 and config[6] ==-1)):
					print("O ganhou!")
					o_win = True
					sair = False			


	m = 0
	for x in range(3):
		for i in range(3):
			matriz[x][i] = config[m]
			m += 1

	print(config)
	print(matriz)
	print(escolha)
	achou = False

	if (x_win):
		config[escolha] = 0
		config = np.append(config,escolha)
		print(config)
		with open('dados.txt') as file:
			for line in file:
				if (line.rstrip('\n') == str(config)):
					achou = True
		if not achou:			
			with open('dados.txt', 'a') as file2:
				file2.write(str(config))
				file2.write("\n")
