n=int(input("Informe um número inteiro: "))
def numPrimo(a):
    if a >1:
        for i in range(2,a):
            if a % i== 0:
                print(a," Não é primo")
                break;
        else:
            print(a," É primo!")
numPrimo(n)