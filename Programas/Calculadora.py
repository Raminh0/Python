from MinhaBF import *
#Main
while True:
    opc = input("Qual operação você quer fazer?\n\n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n0.Sair\n\nOpção: ")
    if opc=="0":
        opc = input("Voçê realmente deseja sair?(0.Sim/2.Não):\n ")
        if opc == "0":
            break
        else:
            continue
    else:
        match(opc):
            case ("1"):
                opc=(input("Deseja somar mais de dois valores?(1.Sim / 2.Não): "))
                match(opc):
                    case "1":
                        valores=[]
                        for i in range(5):
                            valores.append(float(input("Informe o valor ou pressione enter cálculo: ")))
                            #if valores

                        SomarMais(valores)
                        break
                    case "2":
                        a = float(input("Informe o primeiro número para o cálculo: "))
                        b = float(input("Informe o segundo número para o cálculo: "))
                        print(Somar(a,b))
                        break
            case ("2"):
                    a = float(input("Informe o primeiro número para o cálculo: "))
                    b = float(input("Informe o segundo número para o cálculo: "))
                    print(Subtrair(a,b))
                    break
            case ("3"):
                    a = float(input("Informe o primeiro número para o cálculo: "))
                    b = float(input("Informe o segundo número para o cálculo: "))
                    print(Multiplicar(a,b))
                    break
            case ("4"):
                    a = float(input("Informe o primeiro número para o cálculo: "))
                    b = float(input("Informe o segundo número para o cálculo: "))
                    print(Dividir(a,b))
                    break
            case _:
                    print("***OPÇÃO INVÁLIDA!***\nTente novamente.")

        opc = input("Deseja realizar um novo cálculo?(1.Sim/2.Não):\n ")
        if opc == "1":
                break