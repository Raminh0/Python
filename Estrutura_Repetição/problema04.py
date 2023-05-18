sair=0
while (sair!=3):

    n1= float(input("Informe o primeiro valor: "))
    n2= float(input("Informe o segundo vallor: "))
    print("\n1-Para realizar uma operação informe o tipo de operador(+,-,/,*). \n2-Para digitar um novo valor. \n3-Para sair. ")
    opc=input("Opção: ")
    match(opc):
        case ("3"):
            sair=3
        case ("2"):
            print("Ok. Informe novamennte!")
        case ("+"):
            print("O resultado da soma é= ",n1 + n2)
        case ("-"):
            print("O resultado da subtração é= ",n1 - n2)
        case ("*"):
            print("O resultado da multiplicação é= ",n1 * n2)
        case("/"):
            print("O resultado da divisão é= ",n1 / n2)
        case ():
            print("O resultado da multiplicação é= ", n1 * n2)
        case _:
            print("Opção invalida! Tente novamente.")