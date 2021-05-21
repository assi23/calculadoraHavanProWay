#Criação de variáveis, juntamento com a lista das moedas pré-cadastradas
listaMoedas = ["dólar","Dólar","euro","Euro","real","Real"]
moedaOrigem = input(" Insira a moeda de origem dentro dessas moedas pré-cadastradas:" +str(listaMoedas))
moedaDestino = input(" Insira a moeda de destino dentro dessas moedas pré-cadastradas:" +str(listaMoedas))
moedaVlr = float(input("Insira o valor a ser convertido em " +moedaDestino+ ":"))
moedaVlrConvert = ""



#verificação se as moedas estão na lista pré-cadastrada
if (moedaOrigem in listaMoedas and moedaDestino in listaMoedas):
     #se as moedas forem iguais, não é possível executar
     if(moedaOrigem == moedaDestino):
          print("Você não pode converter duas moedas iguais.")
     #se as moedas forem diferentes executa o programa
     if(moedaOrigem != moedaDestino):
          if(moedaOrigem in ["dólar","Dólar"] and moedaDestino in ["real","Real"]):
               moedaVlrConvert = moedaVlr * 5.26
          if(moedaOrigem in ["dólar","Dólar"] and moedaDestino in ["euro","Euro"]):
               moedaVlrConvert = moedaVlr * 0.82
          if(moedaOrigem in ["real","Real"] and moedaDestino in ["dólar","Dólar"]):
               moedaVlrConvert = moedaVlr / 5.26
          if(moedaOrigem in ["real","Real"] and moedaDestino in ["euro","Euro"]):
               moedaVlrConvert = moedaVlr * 0.16 
          if(moedaOrigem in ["euro","euro"] and moedaDestino in ["dólar","Dólar"]):
               moedaVlrConvert = moedaVlr * 1.22 
          if(moedaOrigem in ["euro","euro"] and moedaDestino in ["real","Real"]):
               moedaVlrConvert = moedaVlr * 6.39    
     print("A moeda escolhida para ser convertida foi " +moedaOrigem+ " e a moeda de destino é " +moedaDestino+" e o valor é:"+str(round(moedaVlrConvert, 2)))
else:
      print("As moedas escolhidas não estão na lista.")