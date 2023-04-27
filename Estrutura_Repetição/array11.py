v1=[]
for i in range(1,6):
    print("Valor", i)
    v1.append(int(input()))

pes=int(input("Informe um número para verifocação: "))

conS=0
for y in range(5):
    if pes == v1[y]:
        conS+=1
print("\nO número", pes, " foi encontrado", conS, "vezes")
