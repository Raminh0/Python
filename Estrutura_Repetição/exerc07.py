cont= 0
x= 0

for i in range(1,11):
    print("Informe o",i,"valor: ")
    x=int(input(""))
    if (x >= 10) and (x <= 20):
      cont+=1
print("A qtd de números no intervalo [10,20] é igual: ",cont )
