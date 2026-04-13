from random import shuffle

t1 = input('Digite o nome do primeiro trabalho: ')
t2 = input('Digite o nome do segundo trabalho: ')
t3 = input('Digite o nome do terceiro trabalho: ')
t4 = input('Digite o nome do quarto trabalho: ')

lista = [t1, t2, t3, t4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)