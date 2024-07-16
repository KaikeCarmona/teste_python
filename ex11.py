# 11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO
 
# crio o array que recebera os valores
itens = []

#função que ira adicionar os valores de maneira enfileirada no array
def enfileirar(item):
    itens.append(item)

#função que ira retirar sempre o ultimo elemento do array quando for executada
def desenfileirar( ):
    if itens:
        return itens.pop()
 
# Exemplo de uso

# Adicionando elementos ao array
enfileirar(1)
enfileirar(2)
enfileirar(3)


# Removendo os elementos da lista e atualizando ela
print("Lista: ",itens)
print("o item que saiu da fila foi: ", desenfileirar())  # Saída: 1
print("Lista: ",itens)
print("o item que saiu da fila foi: ",desenfileirar())  # Saída: 2
print("Lista: ",itens)
print("o item que saiu da fila foi: ",desenfileirar())  # Saída: 3
print("Lista: ",itens)