#
# Arquivo de exemplo para uso da classe timedeltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from time import strftime

def QuantosDiasFaltam(ano,mes,dia):
  hoje = date.today()
  dataProdurada = date(ano,mes,dia)

  qtdDias = dataProdurada - hoje

  mensagemRetorno = "Faltam " + str(qtdDias).replace("days, 0:00:00", "") + "dias para a data " + dataProdurada.strftime("%d/%m/%y") #Temn que usar a função str() para converter o objeto tipo data para string, para poder concatenar com outra string
  
  print(mensagemRetorno)

QuantosDiasFaltam(2021,10,29)