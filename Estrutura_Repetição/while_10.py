alunos= int(input("Digite a quantidade de alunos: "))
cont = alunos
soma= 0
while (cont != 0):
    print("Informe a nota do ",cont,"° aluno")
    nota= float(input())
    soma+= nota
    cont-=1
media= soma/alunos
print("A média dos alunos é= ",media)
