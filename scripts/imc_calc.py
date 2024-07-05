def calcular_imc(peso_kg, altura_m):
    """
    Calcula o Índice de Massa Corporal (IMC) dado o peso em quilogramas e a altura em metros.
    :param peso_kg: Peso em quilogramas
    :param altura_m: Altura em metros
    :return: Valor do IMC
    """
    return peso_kg / (altura_m ** 2)

def interpretar_imc(imc):
    """
    Interpreta o valor do IMC e retorna a categoria correspondente.
    :param imc: Valor do IMC
    :return: Categoria do IMC
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obeso"

# Obtenha a entrada do usuário para peso e altura
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# Calcule o IMC
imc = calcular_imc(peso, altura)

# Interprete o IMC
categoria = interpretar_imc(imc)

# Exiba os resultados
print(f"Seu IMC é {imc:.2f}. Você está na categoria: {categoria}.")

