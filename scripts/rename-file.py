import os

pasta = 'C:\\Termos de responsabilidade - GED - 4351\\'

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        original = (os.path.join(diretorio, arquivo))
        novo = original.replace('TERMO DE CIÊNCIA E CONCORDÂNCIA', 'CONTRATO-DESCRICAO-TERMO DE CIÊNCIA E CONCORDÂNCIA I')
        os.rename(original, novo)

#4351-001-APROVDOCCOOPERADOS-NCC-00000000003514-CPF-49157906904-NUMSOL-0001-DESCRICAO-TERMO DE RESPONSABILIDADE-TIPODEAPROVACAO-3157;IniciaFluxo=1;
#TERMO DE CIÊNCIA E CONCORDÂNCIA
