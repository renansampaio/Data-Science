import numpy as np
import random
import os

posicoes = [0,0,0,0,0,0,0,0,0,0]
posicoes_escrito = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
loop = True
pos=''
count = 0

def criaString():
	nova_posicao = ''
	for i in range(10):
		if i < 9:
			nova_posicao = nova_posicao + str(posicoes[i]) + ','
		else:
			nova_posicao = nova_posicao + str(posicoes[9])
	return nova_posicao

def atualizaVetor(usuario,entrada):
	posicoes[entrada] = usuario
	if(usuario == 1):
		posicoes_escrito[entrada] = 'X'
	if(usuario == -1):
		posicoes_escrito[entrada] = 'O'

def printVetor():
	print("       |     |       ")
	print("    {}  |  {}  |  {}    ".format(posicoes_escrito[0],posicoes_escrito[1],posicoes_escrito[2]))
	print(" ______|_____|______ ")
	print("       |     |       ")
	print("    {}  |  {}  |  {}    ".format(posicoes_escrito[3],posicoes_escrito[4],posicoes_escrito[5]))
	print(" ______|_____|______ ")
	print("       |     |       ")
	print("    {}  |  {}  |  {}    ".format(posicoes_escrito[6],posicoes_escrito[7],posicoes_escrito[8]))
	print("       |     |  \n\n")

def gerarExemplo(string):
	with open('exemplo.arff', 'r') as fin:
	    data = fin.read().splitlines(True)
	with open('exemplo.arff', 'w') as fout:
	    fout.writelines(data[:12])
	with open('exemplo.arff', 'a') as f:
	    f.write(string)	    

def posicoesPossiveis():
	print("       |     |       ")
	print("    0  |  1  |  2    ")
	print(" ______|_____|______ ")
	print("       |     |       ")
	print("    3  |  4  |  5    ")
	print(" ______|_____|______ ")
	print("       |     |       ")
	print("    6  |  7  |  8    ")
	print("       |     |  \n\n")


### Função Main ###

print("Bem-Vindo ao Tic-Tac-Toe!! \n")
print("O computador é o 'X' e você é o 'O' \n")
print("Para jogar basta entrar com um dos números indicados no tabuleiro a seguir: \n\n")
posicoesPossiveis()

while (pos != 'iniciar'):
	pos = input("Digite 'iniciar' para comecar\n")

first = random.randint(0,8)
atualizaVetor(1,first)
gerarExemplo(criaString())
printVetor()


while(loop):
	if (count == 4):
		print("Empate!")
		loop = False
		break

	if ((posicoes[0]==1 and posicoes[1]==1 and posicoes[2] ==1) or (posicoes[3]==1 and posicoes[4]==1 and posicoes[5] ==1) or (posicoes[6]==1 and posicoes[7]==1 and posicoes[8] ==1) or (posicoes[0]==1 and posicoes[3]==1 and posicoes[6] ==1) or (posicoes[1]==1 and posicoes[4]==1 and posicoes[7] ==1) or (posicoes[2]==1 and posicoes[5]==1 and posicoes[8] ==1) or (posicoes[0]==1 and posicoes[4]==1 and posicoes[8] ==1) or (posicoes[2]==1 and posicoes[4]==1 and posicoes[6] ==1)):
		print("X ganhou!")
		loop = False
		break

	jogada = input("Posicao da sua jogada:\n")
	while (posicoes[int(jogada)] != 0):
		print("Posica inválida!\n")
		jogada = input("Posicao da sua jogada:\n")

	atualizaVetor(-1,int(jogada))

	if ((posicoes[0]==-1 and posicoes[1]==-1 and posicoes[2] ==-1) or (posicoes[3]==-1 and posicoes[4]==-1 and posicoes[5] ==-1) or (posicoes[6]==-1 and posicoes[7]==-1 and posicoes[8] ==-1) or (posicoes[0]==-1 and posicoes[3]==-1 and posicoes[6] ==-1) or (posicoes[1]==-1 and posicoes[4]==-1 and posicoes[7] ==-1) or (posicoes[2]==-1 and posicoes[5]==-1 and posicoes[8] ==-1) or (posicoes[0]==-1 and posicoes[4]==-1 and posicoes[8] ==-1) or (posicoes[2]==-1 and posicoes[4]==-1 and posicoes[6] ==-1)):
		printVetor()
		print("O ganhou!")
		loop = False
		break

	gerarExemplo(criaString())
	chamada = "java -classpath weka.jar weka.classifiers.rules.JRip -l modelodados.txt -T exemplo.arff -p 0 > output.txt"
	os.system(chamada)
	with open('output.txt', 'r') as arq:
		    classe = arq.read().splitlines(True)
		    classe = classe[5][30]
	if (posicoes[int(classe)] == 0):
		atualizaVetor(1,int(classe))
	else:
		entrada_aleatoria = random.randint(0,8)
		while(posicoes[entrada_aleatoria] != 0):
			entrada_aleatoria = random.randint(0,8)
		atualizaVetor(1,entrada_aleatoria)
	posicoesPossiveis()
	printVetor()
	count = count + 1



