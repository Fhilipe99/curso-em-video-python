distancia = int(input('Qual a distancia da viagem: '))
if distancia <= 200:
    passagem = distancia * 0.50
    print(f'O preço dessa passagem vai sair por {passagem}')
else:
    passagem = distancia * 0.45
    print(f'O preço dessa passagem vai sair por {passagem}')