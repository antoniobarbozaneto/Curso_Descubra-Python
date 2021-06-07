# 
# Arquivo com exemplos para manipulação de dados na Internet
#

import urllib.request

def ConectaInternet():
  objUrl = urllib.request.urlopen("http://www.google.com") #abre o site
  if objUrl.getcode() == 200: # 200 significa que conectou com sucesso!
    dados = objUrl.read() #le o dados da página e armazena na variavel 
    print(dados)

ConectaInternet()

