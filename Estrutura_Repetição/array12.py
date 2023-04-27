nomes=[]
for i in range(1,6):
    print("Informe o ", i, "nome")
    nomes.append(input())

    print("\nRegistroos:")
    for y in range(5):
        print(nomes[y])

print("\nUltimo registro para o primeiro")
for x in range(4,-1,-1):
    print(nomes[x], end="")
