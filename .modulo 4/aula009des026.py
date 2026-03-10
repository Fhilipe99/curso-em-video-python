frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count('a')}')
print(f'A letra "a" aparece pela primeira vez na posição {frase.find('a')+1}')
print(f'A ultima letra "a" aparece na posição {frase.rfind('a')+1}')