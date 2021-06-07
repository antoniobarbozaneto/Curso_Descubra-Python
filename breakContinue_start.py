#
# Exemplo de como usar os comando Break e Continue
#

def loopBreake():
  for x in range(5,10):
    if(x == 7):
      break #Esse comando interrompe o loop
    print("O valor de X é: " ,x)

#loopBreake()

def loopContinue():
  for x in range(5,10):
    if x == 7:
      continue #Esse comando interrompe uma execução e passa para o próximo item. 
    print("O valor de X é: ",x)

loopContinue()