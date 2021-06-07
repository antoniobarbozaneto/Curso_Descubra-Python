#
# Exemplos de como trabalhar com arquivos
#
from genericpath import exists
import os
from os import path
import shutil

def copiaArquivo():
  if path.exists("NovoArquivo.txt"):
    pathAtual = path.realpath("NovoArquivo.txt")
    novoPath = pathAtual + ".bkp"
    shutil.copy(pathAtual,novoPath)#copy serve para a origem e o destino desse arquivo
    shutil.copystat(pathAtual,novoPath) #copystat copia as permissões do arquivo

copiaArquivo()

def renomearArquivo():
  if path.exists("NovoArquivo.txt.bkp"):
    os.rename("NovoArquivo.txt.bkp","ArquivoAlterado2.txt") #os.rename renomeia o arquivo

renomearArquivo()