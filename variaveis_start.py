
# Declarando e inicializando uma variável
f = 0 
print(f)

# declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variáveis de tipos diferentes
print ("isto é uma string " + str(123)) #str é uma função que convete para string

# Variável Global X Variável local 
def AlgumaFuncao(): #A palavra def é para criar uma função.
  global f #Declarando a variavel como global, o valor passado dentro da função será o mesmo que fora dela.
  f  = "def"
  print(f) #O valor declarado aqui e local, está dentro do escopo da função, fora pode usar a mesma variavel com valroes diferentes.

AlgumaFuncao()
print(f)


#Escreve a variavel (f), que é abc lá em cima, é o último valor declarado para a variavel
###################################################################################################
#Outra função TESTE: 

def FuncaoTeste():
  num = 10
  print(num)
FuncaoTeste()


