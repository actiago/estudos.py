""" Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. """
""" A = π R²"""

import math

metrica = input(' - Que tipo de medida irá utilizar? \n 1 - Metro  \n 2 - Centímetro \n Medida: ')
while metrica != '1' and metrica != '2':
    metrica = input('* Escolha o tipo de medida: \n 1 - Metro  \n 2 - Centímetro \n')
    if metrica != '1' and metrica != '2':
        print('* Você deve selecionar uma das opções \n')

if metrica == '1':
    print('\n Selecionada a medida em metro \n')
    valorm = 'M²'
if metrica == '2':
    valorm = 'cm²'
    print('\n Selecionada a medida em centímetro \n')

raio = float(input('- Insira o tamanho do raio a ser calculado: '))

area = math.pi * (raio ** 2)

resultado = 'R: A área do círculo é de {} {}\n'.format(area, valorm)

print('')
print(resultado)

volume_input = input(' - Deseja calcular o volume desta esfera? \n 1 - Sim \n 2 - Não \n Escolha: ' )
while volume_input != '1' and volume_input != '2':
    volume_input = input('* Escolha uma alternativa: \n 1 - Sim \n 2 - Não \n')
    if volume_input != '1' and volume_input != '2':
        print('* Voce deve selecionar uma das opções \n')

if volume_input == '1':
    area_da_superficie = 4 * math.pi * raio ** 2
    volume = (4 / 3) * math.pi * raio ** 3
    resultado_do_raio = 'R: A área da superfície é de {} e o volume da esfera é de {} cm³'.format(area_da_superficie,volume)

    print('')
    print(resultado_do_raio)

if volume_input == '2':
    print('')
    print('Obrigado.\n')
