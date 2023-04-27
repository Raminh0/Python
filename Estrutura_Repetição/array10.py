a=[]
b=[]
c=[]
cont=0
while True:
    try:
        tam = int(input("Informe quantas operações você deseja realizar: "))
    except:
        print("Digite um valor inteiro!\n")
        continue
    for i in range(tam):
        cont+=1
        print(cont,"º Operação: soma")
        a.append(int(input("\nNúmero 1\n")))
        b.append(int(input("\nNúmero 2\n")))
        c.append(a[i] + b[i])
        print("O resultado da ",i,"º soma é: ",c[i])