val = []
valP = []
cont = 0
for i in range(10):
    cont+=1
    print("Informe o valor",cont)
    val.append(int(input("Valor: ")))
valM = val[0]
for a in range(cont):
    if val[a] %2==0:
        valP.append(val[a])
print("Valores pares: ")
for e in range(cont,0,-1):
    print(valP[e])
    #if val[a] > valM:
        #valM= val[a]
