import requests

r = requests.get('http://checkip.amazonaws.com')
print("#" * 33 )
print("\n")
print("Seu ip externo é: {0}".format(r.text))
print("#" * 33)
