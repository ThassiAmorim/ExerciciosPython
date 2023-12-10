

# [5, 3, 1, 8, 3, 7, 2]
# menores [3, 1, 3, 2]
#maiores [5, 8, 7]


def quicksort(vetor):
    #assumindo pivô posição [0]

    if len(vetor) <= 1:
        return vetor
    
    menores = [x for x in vetor[1:] if x < vetor[0]]
    maiores = [x for x in vetor[1:] if x >= vetor[0]]

    return quicksort(menores) + [vetor[0]] + quicksort(maiores)
    


if __name__ == "__main__":
    import random 
    vetor = [random.randint(0,10) for num in range(10)]

    print(vetor)

    print(quicksort(vetor))