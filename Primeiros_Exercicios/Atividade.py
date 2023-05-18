
print("Informe os nomes dos times e a quantidade de gols: \n")
time1= input("Nome do primeiro time: ")
qnt1= int(input("Quantidade de gols: "))
time2= input("Nome do segundo time")
qnt2= int(input("Quantidade de gols: "))
if (qnt1 != qnt2):
    if (qnt1 > qnt2):
        print (time1)
    else:
        print(time2)
else:
    print("O resultado foi empate!")

