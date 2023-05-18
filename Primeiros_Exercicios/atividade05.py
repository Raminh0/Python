n=int(input("Informe um número para saber seu antecessor: "))
if n != 0:
    if n > 0:
        print("O antecessor de", n," é:", n-1)
    else:
        print("O antecessor de", n," é:", n+1)