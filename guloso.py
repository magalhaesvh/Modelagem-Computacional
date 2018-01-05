def guloso(peso, tamanho, capacidade):
    j = tamanho
    x = [0, 0, 0, 0]
    #verifica se o elemento cabe na mochila
    while (j >= 0):
        if peso[j] <= capacidade:
            x[j] = 1
            #caso caiba, e reduzida da capacidade o peso do elemento
            capacidade = capacidade - peso[j]
        j -= 1

    fo = 0
    for i in range(len(valorItens)):
        if x[i] != 0:
          fo = fo + valorItens[i]

    print fo
    return x


aux = [0, 0, 0, 0]
pesoItens = [30, 10, 40, 20]
valorItens = [600,100,840,400]
#faz a razao entre valor e peso para posteriormente ordenar de acordo com esta razao
for i in range(0, 4):
    aux[i] = float(valorItens[i]) / float(pesoItens[i])
#une a razao e o peso e ordena, onde a razao fica sendo 'x' e o peso 'y'
z = zip(aux, pesoItens)
w = zip(aux, valorItens)
z.sort()
w.sort()
print z
#novo vetor de peso ordenado, pegando apenas a posicao 'y'
pesoItens = [y for x, y in z]
valorItens = [y for x, y in w]
print str(pesoItens)

print str(guloso(pesoItens, 3, 50))
