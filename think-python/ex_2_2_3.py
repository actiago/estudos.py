"""Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),
então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar,
que horas chego em casa para o café da manhã?"""

"""
hora_inicial = '6:52' # AM
tempo_primeiro_km = '8:15' # 8 min 15 sec
tempo_tres_km = '7:12' # Por KM
ultimo_km_volta = '8:15' #
"""

import datetime

start_time = '6:52:00'
time_first_km = '0:08:15'
time_tree_km = '0:07:21'
last_time = time_first_km

(h, m, s) = ((start_time, time_first_km, time_tree_km, last_time).split(':'))

convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
total_time = time_first_km + (time_tree_km * 3) + last_time
result = total_time + start_time

print('Chegarei às {} horas para o café da manhã'.format(result))
