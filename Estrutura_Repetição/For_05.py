num= int(input("Informe um número: "))
contPar=0
contImpar=
if (num != 0):
    for i in range (1,num+1):
       # print("os números de 1 até",num,"são: ")
        if (i % 2==0):
            contPar+=1
        else:
            contImpar+=1
else:
        print("Digite um valor diferente de zero")

print("Qtd pares: ",contPar,"\nQtd impares:",contImpar)
