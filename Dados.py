#importando o json para o projeto
import json 

#Abrindo o meu diretorio para buscar as informações do Json
DadosJson = open('../Media de vendas/Dados.json')

#Carregando os dados dentro do Json
Dados = json.load(DadosJson)

#Variaveis 
aux = 0
maior = 0
menor = 0
soma = 0
media = 0

for dia in Dados:
  if(dia ['valor']) != 0:
    aux = dia['valor']

#Calculo do maior faturamento  
  if(aux > maior):
    maior = aux 
    
#Calculo do menor faturamento  
  if(menor == 0):
    menor = aux	
  elif(aux < menor):
    menor = aux
    
  soma += dia ['valor']
  print('O maior valor de faturamento do mês foi: R$ ' + str(maior) + '.') 
  print('O menor valor de faturamento do mês foi: R$ ' + str(menor) + '.') 
  
  #Dividindo a soma pelos dias para chegar na media 
  media = soma / len(Dados) 
  
  #Variavel para mostrar os dias em que o faturamento foi acima da media 
  diasFaturamento = ''
  for i in Dados:
    if(i['valor']) != 0:
      if(i['valor']) > media: 
        diasFaturamento += (str(i['dia']) + ' ')
  print('Os dias de maior faturamento mensal foram: ' + diasFaturamento)