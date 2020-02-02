""" Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. """
""" A = π R²"""

cm = float()
pi = 3.14

metrica = input(' - Que tipo de medida irá utilizar? \n 1 - Metro  \n 2 - Centímetro \n Medida: ')
while metrica != '1' and metrica != '2':
    metrica = input('* Escolha o tipo de medida: \n 1 - Metro  \n 2 - Centímetro \n')
    if metrica != '1' and metrica != '2':
        print('* Você deve selecionar uma das opções \n')

if metrica == '1':
    print('\n Selecionada a medida em metro \n')
    valorm = 'M²'
if metrica == '2':
    cm = metrica * 100
    valorm = 'cm²'
    print('\n Selecionada a medida em centímetro \n')

raio = float(input('- Insira o tamanho do raio a ser calculado: '))

area = pi * (raio ** 2)

resultado = 'R: A área do círculo é de {} {}'.format(area, valorm)

print()
print(resultado)
