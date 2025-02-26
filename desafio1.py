from random import randint

numSorteado = int(randint(1,100)) #sorteia um numero aleatório
tentativa = 0
vcganhou = False
listaDeNumTentados = []
print("Seja bem vindo ao jogo da advinhação\nNeste jogo você tentará acertar em que numero eu estou pensando de 1 a 100")

while vcganhou ==False:   
    try:
        print("Escolha um numero")
        tentativa +=1
        numEscolhido = int(input())
        listaDeNumTentados.append(numEscolhido)
        if numEscolhido > numSorteado: #compara se o num escolhido > que o sorteado
            print("tente um numero menor")
        elif numEscolhido < numSorteado: #compara se o num escolhido < que o sorteado
            print("tente um numero maior")
        else: #senão for < ou > quer dizer que é =, ou seja, o jogador acertou
            print("Você acertou com",str(tentativa),"tentativas!!", sep=" ")
            print("Você tentou",listaDeNumTentados, sep=" ")
            vcganhou = True
    except ValueError:
        print("Insira apenas numeros inteiros")