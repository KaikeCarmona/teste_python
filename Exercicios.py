
#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra

#importando bicliotecas 
import json

# Url para fazer a requisição
response = """[
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]"""

#carregando os ddados do json em formato de string dentro da variavel dados
dados = json.loads(response)

print("\nProdutos com preço maior que 30.00\n")
#Fazendo a varredura no json inteiro
for i in dados:
    #fazendo a varredura dentro da chave produto que é um array de produtos
    for j in i['produtos']:
            #caso o preço do produto seja maior que 30 eu imprimo o nome do produto e o seu preço
            if j['preço'] > 30:
                 print(j['nome'] ,"- R$" , j['preço'],"\n")
            


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import json

#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

# responsejson = """{
#     "nome": "Loja Exemplo",
#     "endereço": {
#         "rua": "Rua Exemplo",
#         "cidade": "Exemplo City"
#     },
#     "produtos": [
#         {"id": 1, "nome": "Produto A", "preço": 29.99},
#         {"id": 2, "nome": "Produto B", "preço": 19.99}
#     ]
# }"""

# varjson = json.loads(responsejson) # Utilizo a biblioteca json para poder manipular o json e carregalo dentro da variavel varjson;
# print(varjson['produtos'][1]['preço']) # Após carregar acessar a variiavel json, acesso a chave produtos (que podemos acessala como um array para pegar o preço de um dos elementos), 
#                                        # depois acesso o preço do elemento de index 1, nocaso o produto B
 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #3- Ordene a lista abaixo em ordem crescente
# #explique detalhadamente por que escolheu essa solução e não outra

# lista = [5,8,3,0,8,1,9,10,20,30]

# # Variaveis para a operação
# listaOrdenada = sorted(lista)

# print(listaOrdenada)

# # Explicação: escolhi o metodo "sorted" pois ele por padrão já existe para 
# # organizar de maneira crescente um array, daria para fazer com pura logica esse processo
# # mas assim poupa-se tempo e memoria da maquina 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


# lista = ["   joao   ","   maria   ","  joana  "]

# lista2 = []

# for i in lista:
#     lista2.append(i.strip())

# print(lista2)

# Explicação: primeiro criei o array lista2, ele ira receber os valores do array lista 
# tratados, depois fiz uma varredura dentro do array lista para poder passar por todos
# os elementos com um FOR, apos isso eu usei o metodo .append para adicionar elementos 
# ao array lista, e passei como parametro do metodo a posição do array lista, o .strip
# é um metodo de string que serve para retirar elementos de uma string.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#5-Retire o segundo item dessa lista e imprima ela:

# lista = [1,2,3,4,5,6]
# segundoItem = lista[1]
# print(segundoItem)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#6-substitua todos os "joao" da lista por "maria"

# lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

# for i in lista:
#     if i == "joao":
#         lista[lista.index(i)] = "maria"
# print(lista)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 7-criar um loop while em Python que itera sobre os itens de uma lista e 
# imprime os itens enquanto o valor de uma variável é menor ou igual a 5. 
# Após imprimir cada item, o valor da variável é incrementado em 1
# explique detalhadamente por que escolheu essa solução e não outra

# lista = [1,2,3,4,5,6,7,8,9]

# i = 0

# while i <= 5:
#     print(lista[i])
#     i += 1
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#8-usando a biblioteca requests, faça uma requisição http para o 
# endpoint https://jsonplaceholder.typicode.com/todos. 
# cada objeto dentro do json possui a chave "completed". 
# que indica se a task foi completada ou não. Faça uma função que trate a 
# resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra


#importando bicliotecas 
# import requests
# import json

# # Url para fazer a requisição
# url = requests.get('https://jsonplaceholder.typicode.com/todos')

# # Função que ira fazer o tratamento dos dados da requisição
# def completed(x):

#     #carregando os dados do json dentro da variavel dados
#     #usei a biblioteca json para facilitar o tratamento dos dados, pois ela transforma o json em uma string
#     dados = json.loads(x.text)

#     #declarando variaveis de controle
#     qtdTrue = 0
#     qtdFalse = 0

#     #percorrendo os dados do json
#     for i in dados:
#         #caso a chave completed seja verdadeira, então a task foi completada, logo ela incrementa +1 a variavel de controle "qtdTrue
#         if i['completed'] == True:
#             qtdTrue += 1
#         #caso contrario incrementa +1 na variavel "qtdFalse"
#         else:
#             qtdFalse += 1
#     #retorno duas strings, uma com a quantidade de tasks completas, e outra com as não concluidas
#     return f"Quantidade de tarefas completas {qtdTrue}", f"Quantidade de tarefas completas {qtdFalse}"

# #chamo a função completed e passo como parametro a url para ser tratada
# res = completed(url)

# #imprimo oque a função completed retorna
# print(res)
 
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os 
# dados retornados faça:
# um parsing de dados e retire  o nome, username, email, rua, numero
# explique detalhadamente por que escolheu essa solução e não outra

#importando bicliotecas 
# import requests
# import json

# # Url para fazer a requisição
# url = requests.get('https://jsonplaceholder.typicode.com/users')

# #carregando os dados do json dentro da variavel dados
# #usei a biblioteca json para facilitar o tratamento dos dados, pois ela transforma o json em uma string
# dados = json.loads(url.text)

# #faço a varredura no json e imprimo no console apenas os elementos que foram solicitados
# for i in dados:
#     print(i['name'] + " - " + i['username'] + " - " +  i['email'] + " - " + i['address']['street'] + " - " +i['phone'],"\n")


#escolhi fazer dessa maneira por ser mais simples e de facil entendimento

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

#crio o array que recebera os valores
# itens = []

 #função que ira adicionar os valores de maneira enfileirada no array
# def enfileirar(item):
#     itens.append(item)

 #função que ira retirar sempre o primeiro elemento do array quando for executada
# def desenfileirar( ):
#     if itens:
#         return itens.pop(0)
 
# # Exemplo de uso

 # Adicionando elementos ao array
# enfileirar(1)
# enfileirar(2)
# enfileirar(3)


 # Removendo os elementos da lista e atualizando ela
# print("Lista: ",itens)
# print("o item que saiu da fila foi: ", desenfileirar())  # Saída: 1
# print("Lista: ",itens)
# print("o item que saiu da fila foi: ",desenfileirar())  # Saída: 2
# print("Lista: ",itens)
# print("o item que saiu da fila foi: ",desenfileirar())  # Saída: 3
# print("Lista: ",itens)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO
 
#crio o array que recebera os valores
# itens = []

# #função que ira adicionar os valores de maneira enfileirada no array
# def enfileirar(item):
#     itens.append(item)

# #função que ira retirar sempre o ultimo elemento do array quando for executada
# def desenfileirar( ):
#     if itens:
#         return itens.pop()
 
# # Exemplo de uso

# # Adicionando elementos ao array
# enfileirar(1)
# enfileirar(2)
# enfileirar(3)


# # Removendo os elementos da lista e atualizando ela
# print("Lista: ",itens)
# print("o item que saiu da fila foi: ", desenfileirar())  # Saída: 1
# print("Lista: ",itens)
# print("o item que saiu da fila foi: ",desenfileirar())  # Saída: 2
# print("Lista: ",itens)
# print("o item que saiu da fila foi: ",desenfileirar())  # Saída: 3
# print("Lista: ",itens)