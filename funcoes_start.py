#
# Arquivo com exemplos de funções
#

# definindo uma função básica
def func1():
  print("Eu sou uma função!")

func1()

# função que recebe argumentos
def func2(arg1,arg2):
  print(arg1+ " " + arg2)

func2("Dani", "Monteiro") # Aqui é passado os parametros para a função, no caso o arg1 e o arg2.

# função que retorna um valor
def cubo(x):
  return x*x*x

f = cubo(3) #Passando para uma variavel o retorno da função, para depois imprimir.
print(f)
#ou
print(cubo(2)) #Imprimindo direto o retorno da função
