import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hipotenusa = math.hypot(ca, co)

print(f'A hipotenusa é: {hipotenusa:.2f}')
