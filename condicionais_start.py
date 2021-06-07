#
# Arquivo de exemplo das estruturas condicionais
#
def Condicionais():
  x,y = 10, 100 #Declarando 2 variaveis e passando os valores diretos para ela. 

  if(x < y): 
    print("X é menor que Y")
  elif( x == y): #elif é igual ao else if
    print("X é igual a Y")
  else:
    print("X é maior que Y")
  Condicionais()