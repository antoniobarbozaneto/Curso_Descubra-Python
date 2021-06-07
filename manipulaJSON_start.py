# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json

def ManipulaJSON():
  endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  webUrl = urllib.request.urlopen(endereco)
  if (webUrl.getcode() == 200):
    dados = webUrl.read()
    oJSON = json.loads(dados) #vai armazenar no objeto json todo o conteudo da pagina em formato json, como um dicionario

    contagem = oJSON["metadata"]["count"] #Dentro dos couchetes [] são as chaves no json que é necessário acessar
    print("Contage:" + str(contagem))

    for local in oJSON["features"]:
      if local["properties"]["place"] == "150 km WSW of Port Orford, Oregon":
        print("Encontrado registro especial! *********")
      else:
        print(local["properties"]["place"]) #Dentro de [properties] eu estou procurado a chave [place] para imprimir o conteudo

ManipulaJSON()