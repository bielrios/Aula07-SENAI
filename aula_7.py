# #Exercício 1 - Crie um número aleatório de 10, 5
import random
print(random.randint(5, 10))

# #Exercício 2 - Crie 3 números aleatórios
import random
print('Primeiro número aleatório:', random.randint(5, 10))
print('Segundo número aleatório:', random.randint(5, 10))
print('Terceiro número aleatório:', random.randint(5, 10))

#Exercício 3 - Crie um número aleatório entre 10 a 30 utilizando o range()
import random
n = random.randrange(1, 30)
#n = random.randint(1, 30)
#for num in range(10, 31):
print(n)