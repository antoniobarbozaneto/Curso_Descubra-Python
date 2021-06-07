#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
import zipfile

def CriaZipModo1():
  shutil.make_archive("ArquivoCompactado","zip","C:\\Users\\neto_\\Desktop\\NETO PANIGASSI\\Cursos (Estudos em casa)\\Python\\Cap. 03")

#CriaZipModo1()

def CriaZipModo2():
  with ZipFile("ArquivoZipModo2.zip","w") as novoZip: #W infica que é um novo arquivo
    #novoZip.write("NovoArquivo.bkp")
    novoZip.write("NovoArquivo.txt")
    #novoZip.write("zipModo1.zip.zip")

#CriaZipModo2()

def DeletaArquivo():
  os.remove("ArquivoCompactado.zip")

#DeletaArquivo()