n1=int(input("\nInforme um número: "))
perg=1
while (n1 != 0) and (perg == 1):
    if n1 > 0:
        print("Número positivo!")
        break
    else:
        print("Número negativo!")
        break
    print("Deseja verificar novamente?(1-Sim / 2-Não)")
    perg=input()
else:
    print("Digite um número diferente de 0.")
