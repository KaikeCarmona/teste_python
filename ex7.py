
# 7-criar um loop while em Python que itera sobre os itens de uma lista e 
# imprime os itens enquanto o valor de uma variável é menor ou igual a 5. 
# Após imprimir cada item, o valor da variável é incrementado em 1
# explique detalhadamente por que escolheu essa solução e não outra

lista = [1,2,3,4,5,6,7,8,9]

i = 0

while i <= 5:
    print(lista[i])
    i += 1

#enquanto o valor do i for menor ou igual a 5, ele ira retornar o valor da posição do array, após isso ele incrementa +1 para passar para a proxima posição do array