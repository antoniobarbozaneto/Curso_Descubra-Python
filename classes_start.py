#
# Exemplo de como criar classes
#

class minhaClasse():
  #Construtor da Classe
  def __init__(self):
    self.meuAtributo = "Passou pelo Construtor!"
##### Métodos que pertencem a classe: minhaClasse
  def meuMetodo(self): #Mtd1
    print("Passou pelo meuMetodo")
    
  def meuMetodo2(self, valor): #Mtd2
    self.OutroAtributo = valor
    print(self.OutroAtributo)
################################################################################
def criaObjeto(): #Criando o objeto
  meuObj = minhaClasse() #Estanciando um objeto do tipo minhaClasse
  var1 = meuObj.meuAtributo #Atribuindo para uma variavel o valor do atributo que está dentro do objeto.
  print(var1)

  meuObj.meuMetodo()

  meuObj.meuMetodo2("Executando um método")

criaObjeto()
