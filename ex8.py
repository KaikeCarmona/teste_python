
# 8-usando a biblioteca requests, faça uma requisição http para o 
# endpoint https://jsonplaceholder.typicode.com/todos. 
# cada objeto dentro do json possui a chave "completed". 
# que indica se a task foi completada ou não. Faça uma função que trate a 
# resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
# explique detalhadamente por que escolheu essa solução e não outra


# importando bicliotecas 
import requests
import json

# Url para fazer a requisição
url = requests.get('https://jsonplaceholder.typicode.com/todos')

# Função que ira fazer o tratamento dos dados da requisição
def completed(x):

    #carregando os dados do json dentro da variavel dados
    #usei a biblioteca json para facilitar o tratamento dos dados, pois ela transforma o json em uma string
    dados = json.loads(x.text)

    #declarando variaveis de controle
    qtdTrue = 0
    qtdFalse = 0

    #percorrendo os dados do json
    for i in dados:
        #caso a chave completed seja verdadeira, então a task foi completada, logo ela incrementa +1 a variavel de controle "qtdTrue
        if i['completed'] == True:
            qtdTrue += 1
        #caso contrario incrementa +1 na variavel "qtdFalse"
        else:
            qtdFalse += 1
    #retorno duas strings, uma com a quantidade de tasks completas, e outra com as não concluidas
    return f"Quantidade de tarefas completas {qtdTrue}", f"Quantidade de tarefas completas {qtdFalse}"

#chamo a função completed e passo como parametro a url para ser tratada
res = completed(url)

#imprimo oque a função completed retorna
print(res)
 