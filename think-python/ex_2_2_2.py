"""Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?"""

capa = 24.95

desconto = capa - 40/100

transporte_primeiro_exemplar = 3

transporte_exemplar_adicional = 0.75

resultado = (desconto * 60) + transporte_primeiro_exemplar + (transporte_exemplar_adicional * 59)

print('O custo total de atacado para 60 cópias do livro é de {} Reais'.format(resultado))
