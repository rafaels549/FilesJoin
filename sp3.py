import os

diretorio = r"C:\Users\Pichau\Desktop\SJC\Sp3"
 
lista_arquivos = os.listdir(diretorio)
print(lista_arquivos)

arquivo_saida = "igs.SP3"

conteudo_total = []

for arquivo in lista_arquivos:
    caminho_completo = os.path.join(diretorio, arquivo)
  
    if os.path.isfile(caminho_completo):
        with open(caminho_completo, "r", encoding="utf-8") as arquivo_atual:
            
            conteudo_total.append(arquivo_atual.read())
with open(arquivo_saida, "w", encoding="utf-8") as arquivo_final:
    for conteudo in conteudo_total:
        arquivo_final.write(conteudo)