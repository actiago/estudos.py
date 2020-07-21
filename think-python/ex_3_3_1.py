"""Exercício 3.1

Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string
com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:

>>> right_justify('monty')
                                                                       monty

Dica: Use concatenação de strings e repetição. Além disso, o Python oferece uma função integrada chamada len,
 que apresenta o comprimento de uma string, então o valor de len('monty') é 5."""

s = str(input('Digite uma palavra aleatória: \n'))

def right_justify(s):
    size = len(s)
    print(sep=' '*(70 - size) + s)

print(right_justify)
