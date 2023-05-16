#Números
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