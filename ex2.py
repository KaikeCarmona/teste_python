
#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

import json

responsejson = """{
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}"""

varjson = json.loads(responsejson)     # Utilizo a biblioteca json para poder manipular o json e carregalo dentro da variavel varjson;
print(varjson['produtos'][1]['preço']) # Após carregar acessar a variiavel json, acesso a chave produtos (que podemos acessala como um array para pegar o preço de um dos elementos), 
                                       # depois acesso o preço do elemento de index 1, nocaso o produto B