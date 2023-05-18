qtdAlun=int(input("Na sala há quantos alunos? "))
alunos=[]
for i in range (1,qtdAlun+1):
    print("Informe o nome do ",i,"º aluno: ")
    nome=input()
    alunos.append(nome)

print("Os nomes dos alunos cadastrados são: ")
for i in range (qtdAlun):
    print(i,".",alunos[i])

busca=input("Buscar nome: ")
for i in range(qtdAlun):
    cont=0
    if (busca == alunos[i]):
        cont+=1
        print(i,".",alunos[i])
if(cont==0):
    print("--Não encontrado--")