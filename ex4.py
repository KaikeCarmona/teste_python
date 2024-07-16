# 4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]

lista2 = []

for i in lista:
    lista2.append(i.strip())
print(lista2)

# Explicação: primeiro criei o array lista2, ele ira receber os valores do array lista 
# tratados, depois fiz uma varredura dentro do array lista para poder passar por todos
# os elementos com um FOR, apos isso eu usei o metodo .append para adicionar elementos 
# ao array lista, e passei como parametro do metodo a posição do array lista, o .strip
# é um metodo de string que serve para retirar elementos de uma string.