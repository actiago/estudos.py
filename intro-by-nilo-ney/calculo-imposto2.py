lucro = float(input("Digite o valor do lucro: "))

imposto = lucro * 0.26

resultado = "Sobre o lucro de R$ %s você deverá pagar R$ %s de imposto" % (lucro,imposto)

print(resultado)
