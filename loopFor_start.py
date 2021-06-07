#
# Arquivo com exemplos de Loops
#

# Definindo um LOOP FOR
def loopFor():
    for x in range(5,10): # (Valor Inicial, Valor Final)
        print(x)

loopFor()

# Usando um LOOP FOR em uma coleção
def loopArray ():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"] # < Um loop dentro desse objeto: Array
    for d in dias:
        print (d)

loopArray()


# Usando BREAK e CONTINUE


# Usando a função enumerate, para buscar valoeres e seus índices
def loopEnum ():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i, d in enumerate(dias): # (i) é o indice que está sendo atribuido para cada posição do Array, no caso o (d)
        print (i, d)

loopEnum()