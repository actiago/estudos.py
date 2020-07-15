"""Inicialize o interpretador do Python e use-o como uma calculadora."""

"Question one variables"

one_min = 60 #seconds
total_min = 42
rest_sec = 42
total_sec = (one_min * total_min) + rest_sec

"Question two variables"

one_mile = 1.61 #kilometers
ten_km = 10 / one_mile

print('01 - Quantos segundos há em 42 minutos e 42 segundos?')
print(f'Resposta - Em um minuto e 42 segundos há {total_sec} segundos')
print()

print('02 - Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.')
print(f'Resposta - Em 10 quilometros há {ten_km} milhas')
print()

print('03 - Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio \n(tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?')
