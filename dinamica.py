import numpy as np
def mochila(peso,valor,tam):
    # linha vai ser o tamanho do peso+1 para contar a linha so com os zeros
    linha = len(peso)+1
    # idem para coluna
    coluna = tam+1
    #inicializa matriz 5xtam toda com zeros
    matriz = np.zeros((5,51), dtype=np.int)
    #preenche a matriz de acordo com as regras
    for i in range(1,linha):
        for j in range(0,coluna):
            if i == 0 or j == 0:
                matriz[i][j] = 0
            elif j < peso[i-1]:
                matriz[i][j] = matriz[i-1][j]
            elif j >= peso[i-1]:
                indice = j - peso[i-1]
                matriz[i][j] = valor[i-1] + matriz[i-1][indice]
    #pega a ultima coluna e joga num vetor
    vetor = [0]
    for i in range(1, linha):
        vetor.append(matriz[i][tam])
    print vetor
    maior = -1
    indice = -1
    #pega o indice do maior elemento da ultima coluna
    for i in range(0,len(vetor)):
        if maior <= vetor[i]:
            maior = vetor[i]
            indice = i

    vetor = [0,0,0,0]
    indice-=1
    while matriz[indice][tam] != 0:
        tam = tam - peso[indice+1]
        vetor[indice] = peso[indice]
        indice-=1
    fo = 0
    for i in range(len(valorItens)):
        if vetor[i] != 0:
            fo = fo + valorItens[i]

    print fo

    return vetor


pesoItens = [30, 10, 40, 20]
valorItens = [600,100,840,400]
print mochila(pesoItens,valorItens,50)