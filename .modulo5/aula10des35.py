r1 = int(input('Digite o primeiro valor da reta: '))
r2 = int(input('Digite o segundo valor da reta: '))
r3 = int(input('Digite o terceiro valor da reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As 3 retas podem formar um triangulo')
else:
    print('Não é possivel formar um triangulo')