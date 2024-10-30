import csv
import boto3

# Inicializa o cliente EC2 com a região especificada
def get_ec2_client(region):
    return boto3.client('ec2', region_name=region)

def get_security_group_rules(ec2_client, security_group_id):
    # Obtém as informações do Security Group
    response = ec2_client.describe_security_groups(GroupIds=[security_group_id])

    # Extrai as regras de ingress e egress
    security_group = response['SecurityGroups'][0]
    ingress_rules = security_group['IpPermissions']
    egress_rules = security_group['IpPermissionsEgress']

    return ingress_rules, egress_rules

def save_rules_to_csv(ingress_rules, egress_rules, file_name):
    # Define os campos que você quer exportar
    fieldnames = ['Type', 'Protocol', 'Port Range', 'Source/Destination', 'Description']

    # Abre o arquivo CSV para escrita
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Função para obter o range de portas corretamente
        def get_port_range(rule):
            if rule.get('IpProtocol') == '-1':  # Protocolo "-1" indica "all"
                return 'all'
            from_port = rule.get('FromPort')
            to_port = rule.get('ToPort')
            if from_port is None or to_port is None:  # Portas ausentes indicam "all"
                return 'all'
            if from_port == to_port:
                return str(from_port)
            return f"{from_port}-{to_port}"

        # Processa as regras de Ingress
        for rule in ingress_rules:
            protocol = rule.get('IpProtocol', 'N/A')
            port_range = get_port_range(rule)

            # Processa IP ranges
            for ip_range in rule.get('IpRanges', []):
                writer.writerow({
                    'Type': 'Ingress',
                    'Protocol': protocol,
                    'Port Range': port_range,
                    'Source/Destination': ip_range.get('CidrIp', 'N/A'),
                    'Description': ip_range.get('Description', 'N/A')
                })

            # Processa IPv6 ranges
            for ipv6_range in rule.get('Ipv6Ranges', []):
                writer.writerow({
                    'Type': 'Ingress',
                    'Protocol': protocol,
                    'Port Range': port_range,
                    'Source/Destination': ipv6_range.get('CidrIpv6', 'N/A'),
                    'Description': ipv6_range.get('Description', 'N/A')
                })

            # Processa grupos de segurança referenciados
            for group_pair in rule.get('UserIdGroupPairs', []):
                writer.writerow({
                    'Type': 'Ingress',
                    'Protocol': protocol,
                    'Port Range': port_range,
                    'Source/Destination': group_pair.get('GroupId', 'N/A'),
                    'Description': group_pair.get('Description', 'N/A')
                })

        # Processa as regras de Egress
        for rule in egress_rules:
            protocol = rule.get('IpProtocol', 'N/A')
            port_range = get_port_range(rule)

            # Processa IP ranges
            for ip_range in rule.get('IpRanges', []):
                writer.writerow({
                    'Type': 'Egress',
                    'Protocol': protocol,
                    'Port Range': port_range,
                    'Source/Destination': ip_range.get('CidrIp', 'N/A'),
                    'Description': ip_range.get('Description', 'N/A')
                })

            # Processa IPv6 ranges
            for ipv6_range in rule.get('Ipv6Ranges', []):
                writer.writerow({
                    'Type': 'Egress',
                    'Protocol': protocol,
                    'Port Range': port_range,
                    'Source/Destination': ipv6_range.get('CidrIpv6', 'N/A'),
                    'Description': ipv6_range.get('Description', 'N/A')
                })

            # Processa grupos de segurança referenciados
            for group_pair in rule.get('UserIdGroupPairs', []):
                writer.writerow({
                    'Type': 'Egress',
                    'Protocol': protocol,
                    'Port Range': port_range,
                    'Source/Destination': group_pair.get('GroupId', 'N/A'),
                    'Description': group_pair.get('Description', 'N/A')
                })

if __name__ == "__main__":
    security_group_id = 'sg-xxxxxx'  # Substitua pelo seu Security Group ID
    region = 'us-east-1'  # Substitua pela sua região desejada

    # Cria o cliente EC2 com a região apropriada
    ec2_client = get_ec2_client(region)

    ingress_rules, egress_rules = get_security_group_rules(ec2_client, security_group_id)

    # Nome do arquivo CSV
    csv_file = 'security_group_rules.csv'

    save_rules_to_csv(ingress_rules, egress_rules, csv_file)
    print(f"Regras exportadas para {csv_file}")

