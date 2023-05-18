#Números
import random
def SomarMais(*n):
    cont=0
    for i in n:
        cont+=i
    return i

def Somar(n1, n2):
    mais = (n1 + n2)
    return mais

def Subtrair(n1, n2):
    menos = (n1 - n2)
    return menos

def Multiplicar(n1, n2):
    vezes= (n1 * n2)
    return vezes

def Dividir(n1, n2):
    divisao=(n1 / n2)
    return divisao
def Preco(pro,qntd,val):
    return pro,qntd*val
#Texto
def Impressao(a,b):
    for i in range(a,b+1):
        for cont in range(a,i):
            print(cont,end=" ")
        print()
def Letras(t):
    cont=0
    for i in t.lower():
        if i != " " and i != ".":
            cont+=1
    print(cont)

def Vogais(a):
    cont=0
    for i in a.lower():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            cont+=1
    return print("Qntd vogais: ",cont)

def forca():

    palavras = ["INAJÁ", "UNIVERSIDADE", "PERNAMBUCO", "BRASIL"]
    acertou = []
    tentativas = 6
    errou = []
    number = random.randint(1, 4)

    match (number):
        case 1:
            palavraSecre = palavras[0]

        case 2:
            palavraSecre = palavras[1]

        case 3:
            palavraSecre = palavras[2]

        case 4:
            palavraSecre = palavras[3]


    print("\n          Jogo da Forca!\n\n")
    print("    A palavra possui", len(palavraSecre), "letras.\n")

    while True:
        letra = input("Digite uma letra: \n")
        letra =letra.upper()

        if letra in acertou or letra in errou:
            print("Você já tentou essa letra. Tente novamente.\n")
            continue

        if letra in palavraSecre:
            acertou.append(letra)
            print("Letra correta!\n")
        else:
            errou.append(letra)
            tentativas -= 1
            print("Letra incorreta!\n")
            print("Você tem", tentativas, "tentativas restantes.\n")

        status = ""
        for letra_secreta in palavraSecre:
            if letra_secreta in acertou:
                status += letra_secreta + " "
            else:
                status += "_ "

        print(status)

        if all(letra in acertou for letra in palavraSecre):
            print("Parabéns! Você venceu!")
            break

        if tentativas == 0:
            print(":(  Você perdeu! A palavra correta era", palavraSecre)
            break
