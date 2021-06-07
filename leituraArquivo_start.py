#
# Lendo arquivos com funções do Python
#

def leituraArquivo():
  arquivo = open("NovoArquivo.txt", "r") #R significa LER/read arquivo.
  if(arquivo.mode == "r"):
    conteudo = arquivo.read() #Méotod read lê todo o conteudo do arquivo e atribui a variavel conteudo.
    print(conteudo)

  arquivo.close()

#leituraArquivo()

def leituraArquivoGrande():
  arquivo = open("NovoArquivo.txt", "r") #R significa LER/read arquivo.
  if(arquivo.mode == "r"):
    conteudoTotal = arquivo.readlines() #readlines() lê linha a linha do arquivo.

    for conteudo in conteudoTotal:
      print(conteudo)

  arquivo.close()

leituraArquivoGrande()