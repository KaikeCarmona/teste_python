#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

for i in lista:
    if i == "joao":
        lista[lista.index(i)] = "maria" #todos os elementos da lista com o i == "joão" receberão o valor "maria"
print(lista)