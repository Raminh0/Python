notas=[]
for i in range(1,5+1):
    print("Informe a nota do",i,"º aluno")
    nota=float(input())
    notas.append(nota)

alunosA=0; alunosR=0; media=0; cont=0
print("Notas dos alunos:")
for i in range(5):
    cont+=1
    print(cont,".",notas[i])
    media=(media + notas[i])/2
    if (notas[i] >= media):
        alunosA+=1
    else:
        alunosR+=1
print("\nA média da turma foi: ",media,"\n\nAlunos aprovados: ",alunosA,"\n\nAlunos reprovados:",alunosR)
