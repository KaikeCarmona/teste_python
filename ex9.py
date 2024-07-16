
# 9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os 
# dados retornados faça:
# um parsing de dados e retire  o nome, username, email, rua, numero
# explique detalhadamente por que escolheu essa solução e não outra

# importando bicliotecas 
import requests
import json

# Url para fazer a requisição
url = requests.get('https://jsonplaceholder.typicode.com/users')

#carregando os dados do json dentro da variavel dados
#usei a biblioteca json para facilitar o tratamento dos dados, pois ela transforma o json em uma string
dados = json.loads(url.text)

#faço a varredura no json e imprimo no console apenas os elementos que foram solicitados
for i in dados:
    print(i['name'] + " - " + i['username'] + " - " +  i['email'] + " - " + i['address']['street'] + " - " +i['phone'],"\n")


# escolhi fazer dessa maneira por ser mais simples e de facil entendimento