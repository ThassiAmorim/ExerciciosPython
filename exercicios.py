
# Online Python - IDE, Editor, Compiler, Interpreter
import random
#-------------------------------------------------

def fatorial(num):
    if(num == 1):
        return num
    else:
        return num*fatorial(num-1)


print(fatorial(5))
#-------------------------------------------------

def palindromo(palavra):
    j = len(palavra)-1
    i = 0;
    while i < j:
        if(palavra[i] != palavra[j]):
            return "não é palindromo"
        i+=1
        j-=1
    return "é palindromo"
    
    
print(palindromo("ovo"))
print(palindromo("pastel"))
print(palindromo("ASDDSA"))

#-------------------------------------------------

vetor = list(range(0,10))
random.shuffle(vetor)

def sorted_caseiro(vetor):
    i=0
    while i < (len(vetor)-1):
        if(vetor[i] > vetor[i+1]):
            aux = vetor[i+1]
            vetor[i+1] = vetor[i]
            vetor[i] = aux
            i = 0
        else:
            i+=1

sorted_caseiro(vetor)            
print(vetor)

#-------------------------------------------------
"""
palavra_adivinhar = "bicicleta"
palavra_atual = ['_']*len(palavra_adivinhar)

print("---- Jogo da forca ----")
for i in range(len(palavra_adivinhar)):
    letra_chute = input("digite uma letra")
    for j in range(len(palavra_adivinhar)):
        if(letra_chute == palavra_adivinhar[j]):
            palavra_atual[j] = letra_chute
            
    palavra_atual_str = ' '.join(palavra_atual)
    print(palavra_atual_str)  
"""
#-------------------------------------------------
frase = "amendoas fritas nao sao legais"
def contar_palavras(frase):
    cont = 1
    for i in range(len(frase)):
        if frase[i] == ' ':
            cont += 1
    return cont
    
print(contar_palavras(frase))
