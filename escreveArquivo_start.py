#
# Escrevendo arquivos com funções do Python
#
def EscreveArquivo():
  arquivo = open("Novo Arquivo.txt","w+") #W significa que o arquivo será escrito, e + significa que se o arquivo não existe deve ser criado.

  arquivo.write("Linha gerada com a função 'EscreveArquivo' \r\n")

  arquivo.close()

def AlteraArquivo():
  arquivo = open("Novo Arquivo.txt","a+") #A significa escreva nas próximas linhas do arquivo, e + significa que se o arquivo não existe deve ser criado.

  arquivo.write("Linha gerada com a função 'AlteraArquivo' \r\n")

  arquivo.close()

EscreveArquivo()