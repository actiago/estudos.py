""" Formula:

    C   F - 32
    - = ------
    5     9

Converter Fahrenheit em Celsius
"""

temperaturaFahrenheit = float(input('Insira a temperatura em Fahrenheit: '))
temperaturaCelsius = (temperaturaFahrenheit - 32) * 5 /9

print('A temperatura em Celsius é: {}'.format(temperaturaCelsius))

