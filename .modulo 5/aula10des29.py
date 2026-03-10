velocidade = int(input('Qual a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'A velocidade maxima é de 80km/h, você estava a {velocidade}km/h, por isso você foi multado, a multa vai sair no valor de {multa}')
else:
    print('Você está dentro do limite de velocidade')