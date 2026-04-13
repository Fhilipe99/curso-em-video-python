nome = input('Digite seu nome: ')

if len(nome) < 4:
    print('Seu nome é curto')
elif len(nome) == 4:
    print('Seu nome é basico')
elif nome == 'Fhilipe':
    print('Seu nome é lindo!!!!')
else:
    print(f'Olá, {nome}')

