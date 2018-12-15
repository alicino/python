# Gerar numeros randomicos/aleatorios e escrever o 
# output em um arquivo .csv
# Total de 250mil linhas
# Numeros aleatorios entre 1 e 9.999

from random import randint

arq = open('rand_python.csv', 'w')

for i in range(0, 250001):
	num = randint(1, 9999)
	arq.write('Python ' +str(i) +': ' +str(num) + '\n')
