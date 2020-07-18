import requests

try:
    dominio = input(' - Digite o domínio que deseja checar o status: \n * Necessário adicionar o prefixo (http:// | https://)  \n :')
    r = requests.head(dominio)
    print(r.status_code)
except requests.ConnectionError:
    print("failed to connect")
