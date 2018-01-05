import random
capacidade = 50
def avaliaSolucao(peso,solucao,valorItens):
    avalia = 0
    valores = 0
    for i in range (0,len(peso)):
        avalia += peso[i] * solucao[i]
        if(avalia<=capacidade and solucao[i] != 0):
            valores += valorItens[i]


    return valores

pesoItens = [30, 10, 40, 20]
valorItens = [600,100,840,400]
melhorSolucao = [0,0,0,0]
solucaoVizinha = [0,0,0,0]
fo = 0
foVizinho = 0
cont = 0
parada = True
while(parada == True):
    solucaoVizinha[random.randint(0, 3)] = 1
    solucaoVizinha[random.randint(0, 3)] = 1
    solucaoVizinha[random.randint(0, 3)] = 1
    solucaoVizinha[random.randint(0, 3)] = 1
    foVizinho = avaliaSolucao(pesoItens,solucaoVizinha,valorItens)
    if(fo < foVizinho):
        melhorSolucao = solucaoVizinha
        fo = foVizinho
        cont = 0
    else:
        solucaoVizinha = [0,0,0,0]
        cont+=1
        if(cont==100):
            parada = False

print "Sua resposta %d" %(fo)

