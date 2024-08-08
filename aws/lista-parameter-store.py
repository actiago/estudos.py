import boto3

# Configurar o boto3 para usar a região us-east-1
ssm = boto3.client('ssm', region_name='us-east-1')

# Nome do arquivo de saída
output_file = 'parameters_with_docdb_prd.txt'

def get_all_parameters():
    """Obter todos os parâmetros do Parameter Store."""
    parameters = []
    next_token = None

    while True:
        if next_token:
            response = ssm.describe_parameters(NextToken=next_token)
        else:
            response = ssm.describe_parameters()

        parameters.extend(response['Parameters'])

        next_token = response.get('NextToken')
        if not next_token:
            break

    return parameters

def get_parameter_value(name):
    """Obter o valor do parâmetro (com descriptografia)."""
    response = ssm.get_parameter(
        Name=name,
        WithDecryption=True
    )
    return response['Parameter']['Value']

def main():
    # Obter todos os parâmetros
    parameters = get_all_parameters()

    # Limpar o arquivo de saída
    with open(output_file, 'w') as f:
        f.write('')

    # Verificar cada parâmetro
    for parameter in parameters:
        parameter_name = parameter['Name']
        parameter_value = get_parameter_value(parameter_name)

        if 'docdb.amazonaws.com' in parameter_value:
            with open(output_file, 'a') as f:
                f.write(f'{parameter_name}\n')

    print(f"Nomes dos parâmetros contendo 'docdb.amazonaws.com' foram salvos em {output_file}")

if __name__ == '__main__':
    main()

