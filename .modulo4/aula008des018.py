import math

angulo = float(input('Digite o valor do angulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno do angulo {angulo} é {seno:.2f}, o cosseno do angulo é {cosseno:.2f} e a tangente do angulo é {tangente:.2f} ')


