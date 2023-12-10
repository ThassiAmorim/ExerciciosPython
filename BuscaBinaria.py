
def busca_binaria(vetor, x):

    inicio = 0
    fim = len(vetor) - 1

    while inicio < fim:
        meio = (inicio + fim)//2
        if x == vetor[meio]:
            return meio
        if x < vetor[meio]:
            fim = meio - 1 
        else:
            inicio = meio + 1

    return -1


if __name__ == "__main__":
    import random

    vetor = sorted([random.randint(0,100) for num in range(100)])
    print(vetor)
    
    print(busca_binaria(vetor, 27))