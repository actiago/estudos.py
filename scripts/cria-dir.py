import os

# Nome do arquivo que contém a lista de diretórios
arquivo = 'diretorios.txt'

# Abre o arquivo para leitura
with open(arquivo, 'r') as file:
    # Lê todas as linhas do arquivo
    linhas = file.readlines()

# Cria cada diretório listado no arquivo
for linha in linhas:
    # Remove espaços em branco e quebras de linha do nome do diretório
    diretorio = linha.strip()

    # Verifica se o nome não está vazio
    if diretorio:
        # Cria o diretório, incluindo subdiretórios se necessário
        os.makedirs(diretorio, exist_ok=True)
        print(f'Diretório "{diretorio}" criado com sucesso!')

print("Todos os diretórios foram criados.")

