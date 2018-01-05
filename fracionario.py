def mochilaFracionaria(peso, indice, capacidade):
    j = indice
    x = [0, 0, 0, 0]
    while (j >= 0):
        #pega o restante(fracao) da capacidade
        if(peso[j]>capacidade and float(capacidade) / peso[j] == 0.5):
            x[j] = 0.5
            break
        elif peso[j]<capacidade:
            #vai pegando os inteiros e descontando o valor da capacidade
            x[j] = 1
            capacidade = capacidade - peso[j]
        j -= 1

    fo = 0
    for i in range(len(valorItens)):
        if x[i] != 0:
            fo = fo + valorItens[i]

    print fo
    return x

aux = [0, 0, 0, 0, 0]
pesoItens = [30, 10, 40, 20]
valorItens = [600,100,840,400]
#faz a razao entre valor e peso para posteriormente ordenar de acordo com esta razao
for i in range(0, 4):
    aux[i] = float(valorItens[i]) / float(pesoItens[i])
#une a razao e o peso e ordena, onde a razao fica sendo 'x' e o peso 'y'
z = zip(aux, pesoItens)
z.sort()
w = zip(aux, valorItens)
w.sort()
#novo vetor de peso ordenado, pegando apenas a posicao 'y'
pesoItens = [y for x, y in z]
valorItens = [y for x, y in w]
print str(pesoItens)
print str(mochilaFracionaria(pesoItens, 3, 50))
