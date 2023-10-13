import os

diretorio = r"C:\Users\Pichau\Desktop\SJC\Base"
diretorio1 = r"C:\Users\Pichau\Desktop\SJC\Navegação"
diretorio2 = r"C:\Users\Pichau\Desktop\SJC\Observação"
lista_arquivos = os.listdir(diretorio)
lista_arquivos1 = os.listdir(diretorio1)

lista_arquivos2 = os.listdir(diretorio2)

arquivo_saida = "SJCBase.14O"
arquivo_saida1 = "SJCNav.14N"
arquivo_saida2 = "SJCObs.14O"


conteudo_total = []
conteudo_total1 = []
conteudo_total2 = []


for arquivo in lista_arquivos:
    caminho_completo = os.path.join(diretorio, arquivo)
  
    if os.path.isfile(caminho_completo):
        with open(caminho_completo, "r", encoding="utf-8") as arquivo_atual:
            
            conteudo_total.append(arquivo_atual.read())
with open(arquivo_saida, "w", encoding="utf-8") as arquivo_final:
    for conteudo in conteudo_total:
        arquivo_final.write(conteudo)
        


for arquivo in lista_arquivos1:
    caminho_completo = os.path.join(diretorio1, arquivo)
    
    if os.path.isfile(caminho_completo):
        with open(caminho_completo, "r", encoding="utf-8") as arquivo_atual:
           
            conteudo_total1.append(arquivo_atual.read())
with open(arquivo_saida1, "w", encoding="utf-8") as arquivo_final:
    for conteudo in conteudo_total1:
        arquivo_final.write(conteudo)
        


for arquivo in lista_arquivos2:
    caminho_completo = os.path.join(diretorio2, arquivo)
    
    if os.path.isfile(caminho_completo):
        with open(caminho_completo, "r", encoding="utf-8") as arquivo_atual:
           
            conteudo_total2.append(arquivo_atual.read())
with open(arquivo_saida2, "w", encoding="utf-8") as arquivo_final:
    for conteudo in conteudo_total2:
        arquivo_final.write(conteudo)
                        
                