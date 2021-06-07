#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def DadosArquivo():
  ArquivoExiste = path.exists("NovoArquivo.txt") #Verifica se existe
  EhDiretorio = path.isdir("NovoArquivo.txt") #Verifica se é um diretório
  pathArquivo = path.realpath("NovoArquivo.txt") #Verifica com o caminho/path
  pathRelativo = path.relpath("NovoArquivo.txt") #Verifica com o caminho/path relativo
  dataCriacao = time.ctime(path.getctime("NovoArquivo.txt")) #Verifica a data de criação do arquivo
  dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt")) #Verifica a data de modificação do arquivo

  print(ArquivoExiste)
  print(EhDiretorio)
  print(pathArquivo)
  print(pathRelativo)
  print(dataCriacao)
  print(dataModificacao)

DadosArquivo()