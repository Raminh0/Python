#Verificar se o númnmero existe na lista e acrescenta-lo caso não exista
#Com logica:
nVerificacao = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8, 1]
def lista (a):

    vetor= []

    for x in a:
        if x not in vetor:
            vetor.append(x)

    return vetor

print("Esses são os números sem repetição informados por  você: ",lista(nVerificacao))

#Com recursos da linguagem:
def lista2(a):

    return list(set(a))

print("Esses são os números sem repetição informados por  você: ",lista2 (nVerificacao))