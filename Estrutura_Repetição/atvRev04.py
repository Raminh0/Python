n1=int(input("Informe o valor 1: "))
n2=int(input("Informe o valor 2: "))
n3=int(input("Informe o valor 3: "))

if (n1 > n3) and (n1 > n2):
    print("O número maior é", n1)
elif (n2 > n1) and (n2 > n3):
    print("O número maior é", n2)
else:
    print("O número maior é", n3)