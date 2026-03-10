import random
palpite = int(input('Advinhe o numero que pensei de 0 a 5: '))
numero = random.randint(0,5)
if palpite == numero:
    print('Você acertou')
else:
    print('Você errou')
