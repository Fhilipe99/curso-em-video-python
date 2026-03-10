salario = float(input('Qual o seu salario: '))
if salario > 1250:
    aumento = salario * 0.10
    print(f'Seu salario teve um aumento de 10%, passando a ser agora {salario+aumento}')
elif salario <= 1250:
    aumento = salario * 0.15
    print(f'Seu salario teve um aumento de 15%, passando a ser agora {salario+aumento}')
