"""O volume de uma esfera com raio r é Fórmula – Volume de uma esfera.. Qual é o volume de uma esfera com raio 5?"""

pi = 3.1415926535897931

raio = float(input('- Insira o tamanho do raio a ser calulado: '))

volume = (4.0/3.0) * pi * raio ** 3

resultado = 'R: Baseado no raio {}, o volume da esfera é de {} cm³'.format(raio,volume)

print('')
print(resultado)
