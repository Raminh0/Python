cont= 0
x= 0
for i in range(10):
    print("Informe o",i,"valor: ")
    x=int(input(""))
    if (x < 0):
      cont+=1
print("A qtd de números negativos são: ",cont )
