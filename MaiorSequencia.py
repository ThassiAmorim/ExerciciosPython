import random

vetor = [random.randint(0,100) for i in range(100)]

def maior_sequencia(vetor):
    maior = []
    aux = []
    
    for i in range(1, len(vetor)):

        aux.append(vetor[i-1])
        if vetor[i-1] > vetor[i]:
            aux = []

        if len(aux) > len(maior):
            maior = aux    

    return maior

print(vetor)
print(maior_sequencia(vetor))

        