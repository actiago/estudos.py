class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = None
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    tiago = Pessoa(nome='Tiago')
    diego = Pessoa(tiago, nome='Diego')
    print(Pessoa.cumprimentar(diego))
    print(id(diego))
    print(diego.cumprimentar())
    print(diego.nome)
    print(diego.idade)
    for filho in diego.filhos:
        print(filho.nome)
