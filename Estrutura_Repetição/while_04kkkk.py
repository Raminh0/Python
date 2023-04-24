n1= int(input("Informe dois valores para realizar a operação de divisão\n\nInforme o primeiro valor: "))
n2= int(input("Informe o segundo valor: "))
while (n1 == 0) or (n2 == 0):
    n2= input("Nenhum número é divisivel por zero.\n\n ***Tente novamente!**\n\nInforme o segunndo valor: ")
divisao= n1/n2
print("Resultado: ",divisao)
