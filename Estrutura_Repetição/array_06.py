a=[]
b=[]
m=[]
cont=0
for i in range(10):
    cont+=1
    a.append(float(input("Informe um número: ")))
    b.append(float(input("Informe mais um valor: ")))
    m.append(a[i] * b[i])
    print("\nO resultado da ",cont,"º operação foi: ",m[i],"\n-----------------------\n")
