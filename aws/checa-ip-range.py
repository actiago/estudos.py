import requests
import json
import ipaddress

# Função para verificar se um range CIDR (subnetwork) está contido em outro
def cidr_in_range(cidr1, cidr2):
    """Verifica se o cidr1 está contido no cidr2"""
    return ipaddress.ip_network(cidr1).subnet_of(ipaddress.ip_network(cidr2))

# Carrega o arquivo de ranges CIDR local
def load_cidrs_from_file(file_path):
    with open(file_path, 'r') as file:
        cidrs = [line.strip() for line in file if line.strip()]
    return cidrs

# Grava os resultados no arquivo de saída
def write_to_output_file(output_file, cidrs_found_in_ranges, cidrs_not_found):
    with open(output_file, 'w') as file:
        # Grava os CIDRs encontrados
        if cidrs_found_in_ranges:
            file.write("CIDRs encontrados nos ranges da AWS:\n")
            for cidr, ranges in cidrs_found_in_ranges.items():
                file.write(f"{cidr} encontrado nos ranges: {', '.join(ranges)}\n")
            file.write("\n")
        else:
            file.write("Nenhum CIDR foi encontrado nos ranges da AWS.\n\n")

        # Grava os CIDRs que não foram encontrados
        if cidrs_not_found:
            file.write("CIDRs não encontrados em nenhum range da AWS:\n")
            for cidr in cidrs_not_found:
                file.write(f"{cidr}\n")
        else:
            file.write("Todos os CIDRs foram encontrados em algum range da AWS.\n")

# URL do arquivo JSON dos IP ranges da AWS
url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

# Faz o download do arquivo JSON
response = requests.get(url)
ip_ranges = response.json()

# Carrega os CIDRs do seu arquivo local
file_path = 'ips.txt'  # Caminho do seu arquivo de CIDRs
cidrs_to_check = load_cidrs_from_file(file_path)

# Filtra os ranges de IPs do JSON
aws_ranges = [prefix['ip_prefix'] for prefix in ip_ranges['prefixes']]

# Validação: verifica se os CIDRs do arquivo estão contidos nos ranges da AWS
cidrs_found_in_ranges = {}

for cidr in cidrs_to_check:
    for aws_range in aws_ranges:
        if cidr_in_range(cidr, aws_range):
            if cidr not in cidrs_found_in_ranges:
                cidrs_found_in_ranges[cidr] = []
            cidrs_found_in_ranges[cidr].append(aws_range)

# Lista CIDRs que não foram encontrados
cidrs_not_found = [cidr for cidr in cidrs_to_check if cidr not in cidrs_found_in_ranges]

# Nome do arquivo de saída
output_file = 'resultado.txt'

# Grava os resultados no arquivo
write_to_output_file(output_file, cidrs_found_in_ranges, cidrs_not_found)

# Mensagem de confirmação
print(f"Resultados gravados no arquivo: {output_file}")

