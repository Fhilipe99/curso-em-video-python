n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'O numero {n1} é maior que o numero {n2} e o numero {n3}')
elif n2 > n1 and n2 > n3:
    print(f'O numero {n2} é maior que o numero {n1} e o numero {n3}')
elif n3 > n1 and n3 > n2:
    print(f'O numero {n3} é maior que o numero {n2} e o numero {n1}')


if n1 < n2 and n1 < n3:
    print(f'O numero {n1} é menor que o numero {n2} e o numero {n3}')
elif n2 < n1 and n2 < n3:
    print(f'O numero {n2} é menor que o numero {n1} e o numero {n3}')
elif n3 < n1 and n3 < n2:
    print(f'O numero {n3} é menor que o numero {n2} e o numero {n1}')


