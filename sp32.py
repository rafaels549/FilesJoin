

import os

diretorio = r"C:\Users\Pichau\Desktop\SJC\Sp3"
arquivo_saida = "arquivo_combinado.sp3"

# Lista para armazenar os conteúdos de todos os arquivos SP3
conteudos_arquivos = []

# Percorre os arquivos SP3 no diretório
for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".sp3"):
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_completo):
            with open(caminho_completo, "r", encoding="utf-8") as arquivo_atual:
                conteudo = arquivo_atual.read()
                conteudos_arquivos.append(conteudo)

# Cria o arquivo de saída e escreve o conteúdo combinado com um cabeçalho de continuidade
with open(arquivo_saida, "w", encoding="utf-8") as arquivo_final:
    # Cabeçalho de continuidade com as datas
    data_inicio = "2014 11 01 00 00 00.0000000"
    data_fim = "2014 11 15 23 59 59.9999999"
    arquivo_final.write("+CONT "+data_inicio+" "+data_fim+"\n")
    
    # Escreve os conteúdos dos arquivos SP3 combinados
    for conteudo in conteudos_arquivos:
        arquivo_final.write(conteudo)

print("Arquivo SP3 combinado gerado com sucesso.")