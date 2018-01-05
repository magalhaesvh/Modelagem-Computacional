import numpy as np
def mochilaInteira(peso, capacidade):
    #gera a matriz de possibilidades
    matriz = np.zeros((16, 4), dtype=np.int)
    for i in range(16):
        num = str(bin(i))
        num = num[2:]
        num.split()
        for j in range(4):
            if j < len(num):
                matriz[i][j + 4 - len(num)] = num[j]
                if matriz[i][j + 4 - len(num)] == 1:
                    matriz[i][j + 4 - len(num)] = peso[j + 4 - len(num)]
    #acha uma solucao com um peso cabivel para cada possibilidade, mas nao consegui chegar na melhor solucao
    solucao = np.zeros((16, 4), dtype=np.int)
    for i in range(16):
        aux = 0
        for j in range(4):
            if matriz[i][j] != 0:
                if matriz[i][j] < capacidade:
                    aux = aux + matriz[i][j]
                    if aux > capacidade:
                        break
                    else: solucao[i][j] = matriz[i][j]
                if matriz[i][j] > capacidade:
                    solucao[i][j] = 0

    print matriz
    print "Solucao:"
    print solucao


pesoItens = [7,3,5,8]
mochilaInteira(pesoItens,10)
















