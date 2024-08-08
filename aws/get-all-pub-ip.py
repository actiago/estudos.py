import boto3
import csv

def get_network_interfaces(region):
    session = boto3.Session(profile_name='default')
    ec2 = session.client('ec2', region_name=region)

    response = ec2.describe_network_interfaces()
    interface_details = []

    for interface in response['NetworkInterfaces']:
        public_ip = interface.get('Association', {}).get('PublicIp')
        if public_ip:
            interface_id = interface['NetworkInterfaceId']
            tags = interface.get('TagSet', [])
            tag_str = ', '.join([f"{tag['Key']}:{tag['Value']}" for tag in tags])
            name = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), 'N/A')
            association = interface.get('Attachment', {}).get('InstanceId', 'N/A')
            description = interface.get('Description', 'N/A')
            interface_details.append({
                'PublicIpAddress': public_ip,
                'Name': name,
                'ResourceType': 'Network Interface',
                'Association': association,
                'Tags': tag_str,
                'Description': description
            })

    return interface_details

def get_nat_gateways(region):
    session = boto3.Session(profile_name='default')
    ec2 = session.client('ec2', region_name=region)

    response = ec2.describe_nat_gateways()
    nat_details = []

    for nat_gateway in response['NatGateways']:
        for address in nat_gateway['NatGatewayAddresses']:
            public_ip = address.get('PublicIp')
            if public_ip:
                nat_gateway_id = nat_gateway['NatGatewayId']
                description = 'N/A'  # NAT Gateways do not have a description field in describe_nat_gateways
                nat_details.append({
                    'PublicIpAddress': public_ip,
                    'Name': 'N/A',
                    'ResourceType': 'NAT Gateway',
                    'Association': nat_gateway_id,
                    'Tags': 'N/A',
                    'Description': description
                })

    return nat_details

def get_load_balancers(region):
    session = boto3.Session(profile_name='default')
    elb = session.client('elbv2', region_name=region)

    response = elb.describe_load_balancers()
    elb_details = []

    for load_balancer in response['LoadBalancers']:
        dns_name = load_balancer.get('DNSName')
        if dns_name:
            elb_name = load_balancer['LoadBalancerName']
            elb_arn = load_balancer['LoadBalancerArn']
            description = load_balancer.get('LoadBalancerArn', 'N/A')  # Load Balancers have ARN as a form of description
            elb_details.append({
                'PublicIpAddress': dns_name,
                'Name': elb_name,
                'ResourceType': 'Load Balancer',
                'Association': elb_arn,
                'Tags': 'N/A',
                'Description': description
            })

    return elb_details

def main():
    regions = ['sa-east-1', 'us-west-2', 'us-east-1']
    all_details = []

    for region in regions:
        all_details.extend(get_network_interfaces(region))
        all_details.extend(get_nat_gateways(region))
        all_details.extend(get_load_balancers(region))

    if all_details:
        with open('public_ip_details_w_desc.csv', 'w', newline='') as csvfile:
            fieldnames = ['Public IP', 'Name', 'Resource Type', 'Association', 'Tags', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for detail in all_details:
                writer.writerow({
                    'Public IP': detail['PublicIpAddress'],
                    'Name': detail['Name'],
                    'Resource Type': detail['ResourceType'],
                    'Association': detail['Association'],
                    'Tags': detail['Tags'],
                    'Description': detail['Description']
                })
    else:
        print("No public IPs found.")

if __name__ == "__main__":
    main()

